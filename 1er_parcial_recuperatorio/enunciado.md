Una empresa familiar de logística de una pequeña localidad desea sistematizar la información de sus envíos para determinar qué tipo de transporte (Bicicleta o Furgoneta) debería utilizar para enviar sus paquetes.

La clase más importante del sistema es *GestorEnvios* que tiene un método gestionarEnvio que dado una lista de transportes disponibles, un paquete y la distancia ingresados por parámetro, determina el mejor transporte posible para el paquete. Esto lo hace preguntando a cada transporte y luego imprime un mensaje indicando la resolución, por ejemplo:

“Gestionando el envío del paquete pesado:

Paquete demasiado pesado para la bicicleta.

El mejor transporte para el paquete es Furgoneta con un factor de 3000.1. Tiempo: 0.16 horas, Costo: 10000.0”

En el caso de no tener ningún transporte posible se debe mostrar el mensaje “No hay transportes disponibles para este tipo de paquete.”

Los paquetes tienen un peso y un volumen, además pueden calcular el peso volumétrico que es el volumen multiplicado por 250, esto es otro indicador que usan las empresas de logística para calcular el valor del envío, ya que pueden existir elementos muy grandes pero con poco peso. Además en esta clase se sobreescribe el método que devuelve una representación del objeto en forma de String (__str__ o toString() ).

En el caso de los transportes, se hace uso de una abstracción que permite abstraer al paquete de las implementaciones específicas. Los métodos que define son: 
   transportarPaquete(double distancia, double pesoPaquete) que devuelve un Double.
    getNombre() que devuelve un String que es el nombre que identifica al transporte.
    tiempoEstimado(double distancia); que devuelve un Double con el tiempo estimado de envío.
    costoEstimado(double distancia); que devuelve un Double con el costo estimado. 

Como implementaciones específicas tenemos Bicicleta que solo puede transportar paquetes que pesan menos o iguales a 5 kg, puede ir a una velocidad promedio de 12 km/h y el valor por km es de 200 pesos. El indicador de conveniencia de transporte que devuelve el método transportarPaquete está dado por la fórmula 0.2 * tiempo +0.8* costo, donde tiempo es lo que tarda según la velocidad promedio y la distancia dada y el costo según la distancia y el valor por km. En el caso de poder transportar el paquete devuelve -1 (de esta forma puede informar al gestor la imposibilidad de transportarlo)

Por último, el otro tipo de transporte es Furgoneta, que puede enviar paquetes con un peso menor o igual a 100 kg, tiene una velocidad promedio de 60km/h y el costo por km es de 1000 pesos. El indicador de conveniencia del transporte está dado por la fórmula 0.7 * tiempo +0.3* costo. Tanto tiempo y costo representan lo mismo que en bicicleta. Note que la fórmula de una furgoneta le da más importancia al tiempo y en el caso de la bicicleta al costo. Al igual que Bicicleta, en el caso de no poder transportarlo devuelve un -1.

### Simulación: 
Instancie dos paquetes uno liviano y otro pesado y solicite al gestor indicar que tipo de transporte es el más indicado. 

¿Qué utilizo para la abstracción de transporte clase (concreta o abstracta) o interfaz? ¿Por qué?

De la opción que no utilizo, realice el planteo para hacer una abstracción de paquete y al menos dos subclases. No es necesario programarlo, solo mencione que clases definiría, métodos y justificación (por ejemplo, porque permite la reutilización, extensión, o una programación abstracta con el uso de polimorfismo).
