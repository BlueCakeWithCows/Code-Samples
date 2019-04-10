/*
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
 */
function f(string, depth = 0){
    let current_line = string.split("\\n", 1)[0];
    let line_depth = (current_line.match(/\\t/g) || []).length;

    if (line_depth !== depth) {
        return [null, string];
    }

    let leftover = string.substr(current_line.length+2, string.length);
    current_line = current_line.substr(2 * line_depth, current_line.length);

    let longest_subpath = "";
    while (1) {

        let results = f(leftover, depth+1);
        let subpath = results[0];
        if (subpath === null) {
            break;
        }

        leftover = results[1];
        longest_subpath = longest_subpath.length < subpath.length ? subpath : longest_subpath;

    }
    return [current_line+ "\\" +longest_subpath, leftover];

}

const query = "dir\\n\\tsubdir1\\n\\t\\tfile1.ext\\n\\t\\tsubsubdir1\\n\\tsubdir2\\n\\t\\tsubsubdir2\\n\\t\\t\\tfile2.ext"
console.log(f(query)[0]);