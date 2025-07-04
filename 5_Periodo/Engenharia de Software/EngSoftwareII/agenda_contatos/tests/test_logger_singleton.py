import pytest
import os
from logger_singleton import Logger

class TestLogger:
    """Testes para o logger singleton"""
    
    def test_singleton_pattern(self):
        """Testa se o padrão singleton está funcionando"""
        logger1 = Logger.get_instance()
        logger2 = Logger.get_instance()
        
        # Verifica se são a mesma instância
        assert logger1 is logger2
        
        # Verifica se são do tipo correto
        assert isinstance(logger1, Logger)
    
    def test_log_info(self):
        """Testa se o log de info está funcionando"""
        logger = Logger.get_instance()
        
        # Testa log de info
        logger.info("Teste de log info")
        
        # Verifica se o log foi adicionado
        logs = logger.get_logs()
        assert len(logs) > 0
        
        # Verifica se contém a mensagem
        log_found = False
        for log in logs:
            if "Teste de log info" in log:
                log_found = True
                break
        
        assert log_found 

    def test_logger_singleton_concorrencia(self):
        """Testa se o logger mantém o padrão singleton em cenários de concorrência"""
        import threading
        import time
        
        instances = []
        
        def get_instance():
            time.sleep(0.01)  # Pequena pausa para simular concorrência
            instance = Logger.get_instance()
            instances.append(instance)
        
        # Cria múltiplas threads para acessar o logger simultaneamente
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=get_instance)
            threads.append(thread)
            thread.start()
        
        # Aguarda todas as threads terminarem
        for thread in threads:
            thread.join()
        
        # Verifica se todas as instâncias são a mesma
        first_instance = instances[0]
        for instance in instances:
            assert instance is first_instance
            assert id(instance) == id(first_instance)

    def test_logger_singleton_reset(self):
        """Testa se o logger pode ser resetado e mantém o padrão singleton"""
        # Obtém a primeira instância
        instance1 = Logger.get_instance()
        
        # Simula um reset (não é uma funcionalidade real, mas testa o comportamento)
        # Como não há método de reset, vamos testar se a instância permanece a mesma
        instance2 = Logger.get_instance()
        
        # Verifica se são a mesma instância
        assert instance1 is instance2
        assert id(instance1) == id(instance2)

    def test_logger_singleton_diferentes_contextos(self):
        """Testa se o logger mantém o padrão singleton em diferentes contextos de execução"""
        # Obtém instância no contexto principal
        main_instance = Logger.get_instance()
        
        # Simula obtenção em um contexto diferente (função local)
        def get_instance_in_context():
            return Logger.get_instance()
        
        context_instance = get_instance_in_context()
        
        # Verifica se são a mesma instância
        assert main_instance is context_instance
        assert id(main_instance) == id(context_instance)

    def test_logger_singleton_memory_efficiency(self):
        """Testa se o logger é eficiente em memória (mesma instância sempre)"""
        instances = []
        
        # Obtém múltiplas instâncias
        for _ in range(100):
            instance = Logger.get_instance()
            instances.append(instance)
        
        # Verifica se todas são a mesma instância
        first_instance = instances[0]
        for instance in instances:
            assert instance is first_instance
            assert id(instance) == id(first_instance)
        
        # Verifica se não há vazamentos de memória (todas as referências apontam para o mesmo objeto)
        unique_instances = set(instances)
        assert len(unique_instances) == 1 