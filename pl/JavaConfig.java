/* JavaConfig - tool for getting paths for current java environment.
 * © 2011  Petr Písař <ppisar@redhat.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

class JavaConfig {
  private static String output = "";


  /*
   * Append text to output with proper padding or terminates if text is null.
   * @param text String to append.
   */
  private static void concatenate(String text) {
    if (text == null) {
      System.exit(2);
    }
    output = (output.equals("") ? ""  : output + " " ) + text;
  }


  /*
   * Show usage message and terminates program with given @exit_code.
   * @param exit_code code to return
   * */
  private static void usage(int exitCode) {
    System.out.print(
        "JavaConfig [OPTIONS]\n" +
        "  --home         Output path to Java home\n" +
        "  --libs-only-L  Output -L linker flags\n"
    );
    System.exit(exitCode);
  }


  /*
   * @Return path to Java home or null in case of error.
   */
  public static String home() {
    return System.getProperty("java.home");
  }


  /*
   * @Return formated libary search path as -L compiler flag,
   * null if error occured.
   * */
  public static String libsOnlyL() {
    String value;
    String paths[];
   
    if (null == (value = System.getProperty("java.library.path"))) {
      return null;
    }

    paths = value.split(":");

    for (int i = 0; i < paths.length; i++) {
      if (paths[i].equals("")) {
        continue;
      }
      
      if (i == 0) {
        value = "-L" + paths[i];
      } else {
        value = value + " -L" + paths[i];
      }
    }

    return value;
  }


  /*
   * Entry point to this class.
   */
  public static void main(String argv[]) {
    if (argv.length < 1) {
      usage(1);
    }

    for (int i = 0; i < argv.length; i++) {
      if (argv[i].equals("--home")) {
          concatenate(home());
      } else if (argv[i].equals("--libs-only-L")) {
          concatenate(libsOnlyL());
      } else {
          usage(1);
      }
    }

    System.out.println(output);
    System.exit(0);
  }
}
