import java.util.ArrayList;

public class CSV {
    private ArrayList<ArrayList<String>> data;

    public CSV() {
        this.data = new ArrayList<>();
    }

    public ArrayList<ArrayList<String>> getData() {
        return data;
    }

    public void setData(ArrayList<ArrayList<String>> data) {
        this.data = data;
    }
}
