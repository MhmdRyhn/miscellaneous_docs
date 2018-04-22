package total.nooflines;

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class TotalNoOfLines {

    private long cnt = 0;

    public long totalLine(String project) throws FileNotFoundException, IOException {
        File dir = new File(project);

        if (!dir.exists() || !dir.isDirectory()) {
            System.out.println("Invalid Path");
            return 0;
        } else {
            File[] files = dir.listFiles();
            
            // for (int i = 0; i < files.length; i++)
            for (File file : files) {
                String newPath = project + "\\" + file.getName();
                if (file.isFile()) {
                    //System.out.println("File Name: " + file.getName());
                    cnt += lineInFile(newPath);
                } else {
                    //System.out.println("Directory Name: " + file.getName());
                    totalLine(newPath);
                }
            }
        }

        return cnt;
    }

    
    private long lineInFile(String path) throws FileNotFoundException, IOException {
        long line = 1;

        File f = new File(path);
        BufferedReader br = new BufferedReader(new FileReader(f));
        String readLine;
        while ((readLine = br.readLine()) != null) {
            line++;
        }

        return line;
    }

    
    
    
    public static void main(String[] args) throws FileNotFoundException, IOException {
        TotalNoOfLines totalLine = new TotalNoOfLines();
        String projectPath = "E:\\\\MyCodes\\\\Rough\\\\Jobtest";
        System.out.println(totalLine.totalLine(projectPath));
    }

}
