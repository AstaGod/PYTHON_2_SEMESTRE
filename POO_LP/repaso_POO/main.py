from rich import print
from rich.markdown import Markdown
edad=20
respuesta="[bold blue]es mayor de edad" if edad>17 else "[italic underline red]es menor de edad"
texto="""
    # titulo
    parrafo
    ```bash
    git commit -m "titulo" -m "cuerpo del commit"
    # comentario
    ```
    # lista
    # lista
    > informacion valiosa
"""
print(respuesta)
mostrar_mark=Markdown(texto)
print(mostrar_mark)