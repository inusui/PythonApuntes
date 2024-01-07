# Interfaces Graficas
Comodo de utilizar, ventanas y todo lo que el usuario ve para facilitar el uso de las aplicaciones. 
De momento solo se a utilizado el terminal para ejecutar comandos o introducirlos al programa por medio del codigo, nunca desde fuera o durante su ejecucion.

## Tkinter

### Widget
Forman Jerarquias

* tk: contenedor base que conforma todos los demas widgets, no tiene tama;o propio sino que se adapta a los demas. 
* frame: marco puede ajustarse a otros contenedores (tk) o Frames
* label: Etiqueta donde se muestra texto. 
* entry: Texto corto.
* text: excribir texto largo conforma varias lineas
* button: selecciona una opcion
* radiio button: selecciona una opcion entre varias
* checkbutton: selecciona una o varias opociones de un grupo
* menu: estructura de botones
* boxes y dialogs: Ventanas emergentes


### frame.pack
#empaquetar a la raiz (side="lado a poner el frame"), anchor="n,s,e,w" (USa los puntos cardinaless)
```frame.pack(side="right", anchor="s") ```

Rellena en X
 ```frame.pack(fill="x")```
para y necesita un segundo parametro ```expand=True```


Se puede rellenar en ambos (both)
 ```frame.pack(fill="both", expand=True)```
