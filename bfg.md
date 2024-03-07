 OpenCV  java -jar C:\Users\Administrator\Downloads\bfg-1.14.0.jar --delete-files *.json

Using repo : C:\Users\Administrator\Desktop\ho\OpenCV\.git

Found 9 objects to protect
Found 4 commit-pointing refs : HEAD, refs/heads/main, refs/remotes/origin/HEAD, refs/remotes/origin/main

Protected commits
-----------------

These are your protected commits, and so their contents will NOT be altered:

 * commit 669f6f0c (protected by 'HEAD')

Cleaning
--------

Found 30 commits
Cleaning commits:       100% (30/30)
Cleaning commits completed in 325 ms.

Updating 1 Ref
--------------

        Ref               Before     After
        -------------------------------------
        refs/heads/main | 669f6f0c | 9d0cf4d9

Updating references:    100% (1/1)
...Ref update completed in 10 ms.

Commit Tree-Dirt History
------------------------

        Earliest                Latest
        |                            |
        ......DDDDDDDDDDDDDDDDDDDDmDmm

        D = dirty commits (file tree fixed)
        m = modified commits (commit message or parents changed)
        . = clean commits (no changes to file tree)

                                Before     After
        -------------------------------------------
        First modified commit | 8f58768c | 9e4fd16a
        Last dirty commit     | 7068ec3f | 395a649f

Deleted files
-------------

        Filename                Git id
        --------------------------------------------------------------
        color_codes.json      | bdba1364 (303.5 MB), 7b5a788e (134 B )
        color_codes_flat.json | ce1eebc9 (265.5 MB), a849e33d (134 B )
        gray_color_codes.json | 6e4795fe (89.0 MB), 0554acea (133 B )


In total, 46 object ids were changed. Full details are logged here:

        C:\Users\Administrator\Desktop\ho\OpenCV.bfg-report\2024-03-07\12-52-37      

BFG run is complete! When ready, run: git reflog expire --expire=now --all && git gc 
--prune=now --aggressive