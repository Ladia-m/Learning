#!/usr/bin/env groovy
import java.io.File

static void main(String[] args) {
    String filename = this.args[0];
    def file = new File(filename);
    if (file.isDirectory()) {
        println "Specified file is a directory!\nContent of directory:";
        file.eachFile() {
            content -> println content.getAbsolutePath();
        }
    } else if (file.isFile()) {
        file.delete();
        println "$filename deleted.";
    }
}
