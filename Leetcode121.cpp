class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int nothold=0;
        int hold=-prices[0];
        for(int i=1;i<prices.size();i++){
            nothold=max(nothold,hold+prices[i]);
            hold=max(hold,-prices[i]);
        }
        return nothold;
        
    }
};
