"""20 cenários comuns de aceitação, executados contra cada CLI original."""
import subprocess
import sys
import unittest
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VALID = ("1", "Estudar", "alta", "2026-12-01")

class CommonCases:
    def run_cli(self, *entries):
        result = subprocess.run(
            [sys.executable, "main.py"], cwd=ROOT / self.folder,
            input="\n".join((*entries, "0")) + "\n",
            capture_output=True, text=True, encoding="utf-8",
            env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"},
            timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("até logo", result.stdout.casefold())
        return result.stdout.casefold()

    def reject(self, *entries):
        out = self.run_cli(*entries, "2")
        self.assertIn("erro:", out)
        self.assertIn("nenhuma tarefa cadastrada", out)

    def test_01_cadastro(self):
        self.assertIn("cadastrada com sucesso", self.run_cli(*VALID))

    def test_02_listagem_campos(self):
        out = self.run_cli(*VALID, "2")
        for field in ("estudar", "alta", "2026-12-01", "pendente"):
            self.assertIn(field, out)
        self.assertRegex(out, r"(?m)^1\s*[.|]\s*estudar")

    def test_03_lista_vazia(self):
        self.assertIn("nenhuma tarefa cadastrada", self.run_cli("2"))

    def test_04_multiplas_tarefas(self):
        out = self.run_cli(*VALID, "1", "Ler", "baixa", "2026-12-02", "2")
        self.assertRegex(out, r"(?m)^1\s*[.|]\s*estudar")
        self.assertRegex(out, r"(?m)^2\s*[.|]\s*ler")

    def test_05_prioridade_media(self):
        self.assertIn("média", self.run_cli("1", "Estudar", "média", "2026-12-01", "2"))
        self.assertIn("cadastrada com sucesso", self.run_cli("1", "Estudar", "média", "2026-12-01"))

    def test_06_prioridade_baixa(self):
        self.assertIn("cadastrada com sucesso", self.run_cli("1", "Estudar", "baixa", "2026-12-01"))

    def test_07_titulo_vazio(self):
        self.reject("1", "", "alta", "2026-12-01")

    def test_08_titulo_espacos(self):
        self.reject("1", "   ", "alta", "2026-12-01")

    def test_09_prioridade_invalida(self):
        self.reject("1", "Estudar", "urgente", "2026-12-01")

    def test_10_prioridade_vazia(self):
        self.reject("1", "Estudar", "", "2026-12-01")

    def test_11_prazo_vazio(self):
        self.reject("1", "Estudar", "alta", "")

    def test_12_dia_inexistente(self):
        self.reject("1", "Estudar", "alta", "2026-02-30")

    def test_13_mes_inexistente(self):
        self.reject("1", "Estudar", "alta", "2026-13-01")

    def test_14_formato_incorreto(self):
        self.reject("1", "Estudar", "alta", "01/12/2026")

    def test_15_ano_bissexto(self):
        self.assertIn("cadastrada com sucesso", self.run_cli("1", "Estudar", "alta", "2028-02-29"))

    def test_16_conclusao(self):
        out = self.run_cli(*VALID, "3", "1", "2")
        self.assertRegex(out, r"(?m)^1\s*[.|].*estudar.*concluída")

    def test_17_id_inexistente(self):
        out = self.run_cli(*VALID, "3", "99", "2")
        self.assertIn("erro:", out)
        self.assertRegex(out, r"(?m)^1\s*[.|].*estudar.*pendente")

    def test_18_id_nao_numerico(self):
        self.assertIn("erro:", self.run_cli(*VALID, "3", "abc"))

    def test_19_id_zero(self):
        self.assertIn("erro:", self.run_cli(*VALID, "3", "0"))

    def test_20_conclusao_isolada(self):
        out = self.run_cli(*VALID, "1", "Ler", "baixa", "2026-12-02", "3", "2", "2")
        self.assertRegex(out, r"(?m)^1\s*[.|].*estudar.*pendente")
        self.assertRegex(out, r"(?m)^2\s*[.|].*ler.*concluída")

class TestAsk(CommonCases, unittest.TestCase):
    folder = "ia_assistiva"

class TestAgent(CommonCases, unittest.TestCase):
    folder = "agente_ia"

if __name__ == "__main__":
    unittest.main(verbosity=2)
