import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;

public class MapReduce {

    public static String textFilePath = "../textFiles/";

    public static void main(String[] args) {
        if(args.length > 0) {
            for (int i = 0; i < args.length; i++) {
                String fileName = args[i];
                //System.out.println(fileName);

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

                            //Metemos palabra en el HashMap o actualizamos

                            for(int j=0; j < splitLine.length; j++){
                                if (palabras.get(splitLine[j]) == null) {
                                    palabras.put(splitLine[j], 1);
                                } else {
                                    palabras.put(splitLine[j], palabras.get(splitLine[j]) + 1);
                                }
                            }
                        }



                        input.close();

                        BufferedWriter writer = new BufferedWriter(new FileWriter(textFilePath+"RES_"+i+"_"+fileName ));
                        
                        System.out.println("Iteracio: " + i);
                        System.out.println("-------------------------");
                        for (String k: palabras.keySet()) {
                            System.out.println(k + " : " + palabras.get(k) + "\n");
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

}
