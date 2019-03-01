import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;

public class MapReduce {

    public static String textFilePath = "textFiles/";

    public static void main(String[] args) {

        if(args.length > 0) {
            String fileName = args[0];

            //TODO
            //Si hay más de un doc, hacer un foreach y llamar a su splitter y mapper

            //Lectura fichero
            try {
                BufferedReader input = new BufferedReader(new FileReader(textFilePath + fileName));

                //Creamos HashMap
                HashMap<String, Integer> palabras = new HashMap<String, Integer>();

                //Split
                try {
                    String linea;
                    String[] splitLine;

                    while ((linea=input.readLine()) != null) {
                        //Map
                        //Limpiamos linea
                        linea = linea.toLowerCase();
                        linea = linea.replaceAll("([^\\w\\s'-])","");

                        //Separamos palabras
                        splitLine = linea.split(" ");

                        //while

                        //TODO
                        //Metemos solo la primera palabra de cada frase (hay que hacerlo recursivo)
                        //No es capaz de sumar palabras iguales

                        //Metemos palabra en el HashMap o actualizamos

                        for(int i=0; i < splitLine.length; i++){
                            if (palabras.get(splitLine[i]) == null) {
                                palabras.put(splitLine[i], 1);
                            } else {
                                palabras.put(splitLine[i], palabras.get(splitLine[i]) + 1);
                            }
                        }
                    }

                    input.close();

                    BufferedWriter writer = new BufferedWriter(new FileWriter(textFilePath+"Resultat"+fileName));

                    for (String k: palabras.keySet()) {
                        writer.write(k + " : "+palabras.get(k)+"\n");
                    }
                    writer.close();

                }
                catch(Exception e){
                    System.out.println("Error Lectura Fichero");
                }
            }
            catch(Exception e){
                System.out.println("Error Apertura Fichero");
            }


        }
    }
}
