##  un hash y por qué es tan importante para la seguridad digital?

Hash y función de hash no son lo mismo, el primero es el resultado y el segundo es el proceso criptográfico mediante el cuál se obtiene. Los resultados son identificadores únicos e irrepetibles a partir de una información dada.

En definitiva, este término es una pieza clave en la tecnología blockchain y para la seguridad de la información digital de las empresas, siendo capaz de integrar sus funcionalidades en herramientas que son ampliamente utilizadas como la firma electrónica.

Lee hasta el final este contenido, te vamos a conversar más sobre qué es el hash, sus propiedades y 4 de sus principales usos prácticos.

Hash: ¿de qué trata esta tecnología?
Una función “hash” criptográfica es, como su nombre lo indica, una función matemática utilizada en criptografía donde las más comunes agarran entradas de longitudes versátiles para restituir salidas de una longitud permanente.

A su vez, combina las capacidades de paso de mensajes hash con propiedades de ciberseguridad.

Entre los puntos claves para comprender este término encontramos:

Transforman o “monitorean” un conjunto de datos mediante operaciones matemáticas en una cadena de bits de tamaño constante, también conocido como “valor hash”.
Son empleados en criptografía, cuentan con niveles inconstantes de complejidad.
El uso más arraigado de esta tecnología es para las criptomonedas, seguridad de contraseña y de mensajes.
A decir verdad, ¿cómo funcionan las funciones hash?
Las funciones hash son estructuras de datos de uso común en los sistemas informáticos para tareas, como verificar la integridad de los mensajes y autenticar la información.

Agregan características de seguridad a las funciones típicas, lo que dificulta la detección del contenido de un mensaje o información sobre destinatarios y remitentes; en particular exhiben estas tres propiedades:

Están libres de colisiones o “collision-free”: significa que no se deben asignar dos hashes de entrada al mismo hash de salida.
Pueden ocultarse: debería ser difícil adivinar el valor de entrada de una función hash a partir de su salida.
Deben ser amigables con los rompecabezas: tiende a ser complicado seleccionar una entrada que proporcione una salida predefinida, por lo tanto, debe ser elegida de una distribución que sea lo más amplia posible.
Las tres propiedades que acabamos de describir son deseables, sin embargo, no siempre pueden implementarse en la práctica. 

Por ejemplo, la disparidad en los espacios de muestra para valores hash de entrada y las salidas asegura que las colisiones sean posibles

4 ejemplos de funciones hash que refuerzan la seguridad digital empresarial
Las funciones de hash criptográficas se utilizan ampliamente en las criptomonedas para pasar información de transacciones de forma anónima. Por ejemplo, Bitcoin, la criptomoneda original y más grande, utiliza la función hash SHA-256 en su algoritmo.

No obstante, los hash tienen otras aplicaciones. Estas son 4 de las más comunes:

1. Verificación de contraseña
Almacenar contraseñas en un archivo de texto normal es peligroso, por lo que casi todos los sitios guardan sus passwords como hashes.

Cuando un usuario ingresa sus datos, se aplica un hash y el resultado se compara con la lista de valores resguardados en los servidores de la empresa. 

Ciertas propiedades afectan la seguridad del almacenamiento de contraseñas, incluyendo:

No reversibilidad o unidireccionalidad: un buen hash debería dificultar la reconstrucción de la clave original a partir de la salida o de este mismo.
Efecto de difusión o avalancha: un cambio en un solo bit tendría que resultar en una modificación a la mitad de los bits del hash. En otras palabras, cuando una contraseña se cambia ligeramente, la salida del texto cifrado debería cambiar de manera significativa e impredecible.
Determinismo: una password determinada siempre debe generar el mismo valor hash o texto cifrado.
Resistencia a colisiones: tiende a ser dificultoso encontrar dos claves diferentes que tengan como hash en el mismo texto cifrado.
Impredecible: el valor no debe ser predecible a partir de la contraseña.
2. Comprobación de la integridad de los archivos y mensajes
Se pueden usar hashes para asegurarnos de que los mensajes y archivos transmitidos del remitente al receptor no sean manipulados en el transcurso de la transacción; la práctica construye una “cadena de confianza”.

3. Hashing y ciberseguridad
Cuando una empresa descubre que las contraseñas de una plataforma se han visto comprometidas, generalmente significa que los hackers han adquirido los hash que representan a estas.

Luego, los piratas informáticos ejecutan los hash de palabras comunes y combinaciones de palabras y números comunes para descifrar algunas de las claves que los usuarios han resguardado.

La industria de la ciberseguridad se encuentra utilizando un mecanismo denominado “salting”; su traducción libre y directa es “salazón”.

Entonces, “salar” incluye agregar datos aleatorios a una contraseña antes de aplicar el hash y luego almacenar ese “valor de sal” junto con este. Este proceso dificulta que los hackers usen técnicas de cálculo previo y descifrar las contraseñas de los datos hash que han adquirido.

4. Generación y verificación de firmas electrónicas
La verificación de firmas es un proceso matemático que se usa para comprobar la autenticidad de documentos o mensajes digitales.

Una firma electrónica es válida cuando se cumplen los requisitos previos, le da a su receptor una prueba sólida que el mensaje fue creado por un remitente conocido y que no ha sido alterado en tránsito.

Un esquema de este tipo generalmente consta de tres algoritmos de:

Generación de claves;
Firma que, dado un mensaje y una clave privada, genera la rúbrica electrónica;
Verificación de firmas.

- Al momento de que el firmante firma un documento, este se crea utilizando la clave privada de la persona; el algoritmo matemático actúa como un cifrado, creando datos que coinciden con el documento firmado, llamado hash, y encriptando esa información.
-----------------------------------------------------------------------------------------------------------------
## Hash Table


La estructura de datos de la tabla Hash almacena elementos en pares clave-valor donde

Clave- número entero único que se utiliza para indexar los valores Valor- datos que se asocian a las claves.

![Capture](https://user-images.githubusercontent.com/124454895/232366494-6e0140e2-37e5-4ed1-aa32-6cb04d677853.PNG)




