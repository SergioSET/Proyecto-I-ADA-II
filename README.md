## Proceso de instalación
***
Para poder ejecutar los algortimos porfavor siga los pasos descritos abajo. 

Deberá instalar Git en su máquina local, puede encontrarlo en: https://git-scm.com/downloads

También deberá contar con una versión de python en su máquina, se recomienda: https://www.python.org/downloads/

Además deberá instalar Pip para python, este proceso es variante según su sistema operativo, se recomienda seguir los pasos del siguiente link: https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/

Una vez todo esté correctamente instalado vaya al directorio donde desea tener los archivos del repositorio y ejecute los siguientes comandos:
```
git clone https://github.com/SergioSET/Proyecto-I-ADA-II.git
cd Proyecto-I-ADA-II/
pip install -r requirements.txt
python3 main.py
```
Si todo funciona correctamente, verá que se abre un selector de archivos en la ruta de ejemplos que nos fueron proporcionados en el curso, si desea cambiar a otro archivo puede navegar libremente, tenga en cuenta que el tipo de archivo por defecto que mostrará será ".sub", si desea proporcionar ejemplos de la solución dinámica modificada puede cambiar el tipo de archivo. Tenga en cuenta que al seleccionar tipo de archivos ".sub", solo se le mostrarán los algoritmos que admiten ese tipo de entradas, siendo así Fuerza bruta, Voraz, Dinámica; si ingresa un archivo tipo ".psub" se le mostrará únicamente la Dinámica modificada.

Después de seleccionar el archivo podrá seleccionar el algoritmo a probar, se mostrará un mensaje diciendo que empezará a ejecutarse, al cerrar esta ventana, el algoritmo empezará a funcionar y se le notificará que terminó con una nueva ventana indicandole datos de la ejecución. Tenga en cuenta que si el archivo de entrada no cumple con las condiciones o parametros dados, es posible que surga errores que se mostrarán en la consola donde ejecutó el programa.

Si usted ejecuta estos algoritmos desde un sistema Windows, está implementada una función que al finalizar el algoritmo se abrirá el txt correspondiente con la solución, sin embargo, si ejecuta en otro sistema operativo esta funcionalidad no estará disponible, y deberá acceder mediante un explorador de archivos al archivo .txt correspondiente al algoritmo que ejecutó.

Por último, si desea volver a ejecutar el programa solo debe colocar el siguiete comando:
```
python3 main.py
```

nota: Es importante notar que sí ejecuta el programa en un sistema diferente de Windows es probable que la imagen de la interfaz gráfica no se muestre correctamente, cabe resaltar que es recomendable no presionar la imagen, ya que podría dar entradas erróneas al código.
