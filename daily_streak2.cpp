#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumDeletions(string s) {
        int total_a = count(s.begin(), s.end(), 'a');
        int left_b = 0;

        // Initial split: all characters on the right
        int ans = total_a;

        for (char c : s) {
            if (c == 'a') {
                total_a--;  // one fewer 'a' on the right
            } else { // c == 'b'
                left_b++;  // one more 'b' on the left
            }
            ans = min(ans, left_b + total_a);
        }

        return ans;
    }
};

int main() {
    Solution sol;

    // Test examples
    cout << sol.minimumDeletions("aababbab") << endl; // 2
    cout << sol.minimumDeletions("bbaaaaabb") << endl; // 2
    cout << sol.minimumDeletions("b") << endl; // 0

    return 0;
}
