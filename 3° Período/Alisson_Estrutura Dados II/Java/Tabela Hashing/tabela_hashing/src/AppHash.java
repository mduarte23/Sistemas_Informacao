import java.util.HashMap;
import java.util.HashSet;

public class AppHash {
    public static void main(String[] args) {
        HashSet<String> conjunto = new HashSet<String>();
        conjunto.add("laranja");
        conjunto.add("morango");
        System.out.println(conjunto);

        HashMap<String, Integer> mapa = new HashMap<String, Integer>();
        mapa.put("ABC-7854", 8741);
        mapa.put("PUT-0800", 784251);
        System.out.println(mapa.get("ABC-7854"));
    }
}
