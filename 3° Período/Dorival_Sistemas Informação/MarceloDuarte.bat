@echo off
setlocal

set "arquivo1=daeonline.pdf"
set "arquivo2=Profile.pdf"
set "resultado=resultado_comparacao.txt"  rem Adicionei o nome do arquivo de resultado

fc "%arquivo1%" "%arquivo2%" > nul  rem Redirecionei a saída para nul para evitar mostrar a saída na tela

if errorlevel 1 (
    echo Arquivos são diferentes. > "%resultado%"  rem Usei um único > para sobrescrever o arquivo
) else (
    echo Arquivos são iguais. > "%resultado%"  rem Usei um único > para sobrescrever o arquivo
)

endlocal