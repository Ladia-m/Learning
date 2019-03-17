#!/usr/bin/env groovy
import java.io.File

class WriteAndRead {
    static void create_file(def filename) {
        new File('./',filename).withWriter('utf-8') {
            writer -> writer.writeLine 'Hello World!\nShowing how to write into files in groovy';
            writer.writeLine 'Another command';
            def lines = ['line1', 'line2', 'line3'];
            for(String line : lines) {
                writer.writeLine line;
            }
        }
    }
    static void get_file_size(def filename) {
        File file = new File(filename);
        println "The file ${file.absolutePath} has ${file.length()} bytes."
    }
    static read_file(def filename) {
        List lines = [];
        def counter = 0;
        new File('./' + filename).eachLine {
            line -> lines.add("$line");
            counter++;
            println "Reading line #$counter";
        }
        return lines;
    }
/** Reading whole file at once:
    static void read_lines2(def filename) {
        file file = new file('./' + filename)
        println file.text
    }
*/
    static void print_lines(def lines) {
        for(String line : lines) {
            println line;
        }
    }
    static void main(String[] args) {
        String filename = 'example_file.txt';
        println "\nCreating " + filename + " ..";
        create_file(filename);
        println filename + "$filename created.";
        get_file_size(filename);
        println "\nLoading file..."
        def lines = read_file(filename);
        println "\nPrinting content:";
        print_lines(lines);
    }
}
