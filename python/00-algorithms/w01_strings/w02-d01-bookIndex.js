    /* 
    Book Index

    Given an array of ints representing page numbers
    return a string with the page numbers formatted as page ranges when the nums
    span a consecutive range.
    */

    const nums1 = [1, 13, 14, 15, 37, 38, 70];
    const expected1 = "1, 13-15, 37-38, 70";

    const nums2 = [5, 6, 7, 8, 9];
    const expected2 = "5-9";

    const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
    const expected3 = "1-3, 7, 9, 15-17";


    // function bookIndex(nums) {
    //     var expected = ""
    //     for (var i = 0; i< nums.length;i++) {
    //         var pageIndex = i
    //         var currentNumber = nums[i]
    //         if(currentNumber+1!= nums[i+1]){
    //             if(i== nums.length-1){
    //                 expected+=currentNumber
    //             }else{
    //                 expected+=currentNumber+", "
    //             }
    //         } else{
    //             while(nums[pageIndex+1] - nums[i] == 1){
    //                 pageIndex+=1
    //                 i = pageIndex
    //                 console.log(i);
    //             }
    //             expected += currentNumber+"-"+nums[i]+", "
    //         }
    //     }
    //     return expected
    // }
    // function bookIndex(nums) {
    //     var expected = ""
    //     for (var i = 0; i< nums.length;i++) {
    //         if(nums[i]!= nums[i-1]+1){
    //             if(i!=0){
    //                 expected+=", "
    //             }
    //                 expected+= nums[i]
    //         }  else if ()
    //     }
    //     return expected
    // }
    function bookIndex(nums) {
        var expected = ""
        var start = 0
        for (var i = 0; i< nums.length;i++) {
            var end = i
            //  nums[0]+1 = 2         nums[0+1] =  13
            // No range single value 
            if(nums[i]+1 != nums[i+1]){
                if(start == end){
                    if(i == nums.length -1){
                        expected += nums[i]
                    } else {
                        expected += nums[i]+", "
                    }
                } 
                else {
                //    console.log(nums[start], "-----", nums[end]);
                expected += nums[start] + "-" + nums[end]+", "
                }
                start = i+1
            }
        }
        return expected
    }
    console.log(bookIndex(nums2))