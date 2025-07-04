#!/usr/bin/env python3
"""
Script para testar as ferramentas de qualidade de código localmente.
Este script simula os passos dos workflows do GitHub Actions.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Executa um comando e retorna o resultado."""
    print(f"\n🔍 {description}")
    print(f"Comando: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            print("✅ Saída:")
            print(result.stdout)
        if result.stderr:
            print("⚠️  Avisos/Erros:")
            print(result.stderr)
        print(f"📊 Código de saída: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")
        return False

def main():
    """Função principal que executa todos os testes."""
    print("🚀 Iniciando testes de qualidade de código...")
    print("=" * 60)
    
    # Verificar se estamos no diretório correto
    if not Path("requirements.txt").exists():
        print("❌ Erro: Execute este script no diretório raiz do projeto")
        sys.exit(1)
    
    # Lista de comandos para executar
    commands = [
        ("python -m pytest tests/ -v", "Executando testes"),
        ("python -m pytest tests/ --cov=Controller --cov=Model --cov-report=term-missing", "Testes com cobertura"),
        ("safety check", "Verificando vulnerabilidades de segurança"),
        ("bandit -r . -f txt", "Análise estática de segurança"),
        ("flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127", "Verificação de estilo de código"),
        ("black --check --diff .", "Verificação de formatação"),
        ("isort --check-only --diff .", "Verificação de organização de imports"),
    ]
    
    results = []
    
    for command, description in commands:
        success = run_command(command, description)
        results.append((description, success))
    
    # Resumo dos resultados
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for description, success in results:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{status}: {description}")
        if success:
            passed += 1
        else:
            failed += 1
    
    print(f"\n📈 Resultado Final: {passed}/{len(results)} testes passaram")
    
    if failed > 0:
        print(f"⚠️  {failed} teste(s) falharam. Verifique os logs acima.")
        sys.exit(1)
    else:
        print("🎉 Todos os testes passaram! Código pronto para commit.")

if __name__ == "__main__":
    main() 