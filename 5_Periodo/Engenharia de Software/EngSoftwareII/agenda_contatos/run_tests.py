#!/usr/bin/env python3
"""
Script para executar os testes da aplicação de agenda de contatos
"""

import subprocess
import sys
import os

def run_tests():
    """Executa os testes usando pytest"""
    print("🚀 Iniciando execução dos testes...")
    print("=" * 50)
    
    # Comando base do pytest
    cmd = [
        sys.executable, "-m", "pytest",
        "-v",
        "--tb=short",
        "--cov=.",
        "--cov-report=html",
        "--cov-report=term-missing"
    ]
    
    try:
        # Executa os testes
        result = subprocess.run(cmd, cwd=os.path.dirname(__file__))
        
        print("\n" + "=" * 50)
        if result.returncode == 0:
            print("✅ Todos os testes passaram com sucesso!")
        else:
            print("❌ Alguns testes falharam!")
        
        print(f"\n📊 Relatório de cobertura gerado em: htmlcov/index.html")
        print(f"📁 Para ver o relatório detalhado, abra: htmlcov/index.html no seu navegador")
        
        return result.returncode
        
    except FileNotFoundError:
        print("❌ Erro: pytest não encontrado. Instale com: pip install pytest pytest-cov")
        return 1
    except Exception as e:
        print(f"❌ Erro ao executar testes: {e}")
        return 1

def run_specific_test(test_file=None):
    """Executa um teste específico"""
    if not test_file:
        print("❌ Especifique um arquivo de teste")
        return 1
    
    cmd = [sys.executable, "-m", "pytest", "-v", test_file]
    
    try:
        result = subprocess.run(cmd, cwd=os.path.dirname(__file__))
        return result.returncode
    except Exception as e:
        print(f"❌ Erro ao executar teste: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Executa teste específico
        test_file = sys.argv[1]
        exit_code = run_specific_test(test_file)
    else:
        # Executa todos os testes
        exit_code = run_tests()
    
    sys.exit(exit_code) 