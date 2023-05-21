#include <cs50.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    int luhnealgorethim(string credit);
    bool iscredit(int finalsum);
    string CreditType(string credit);
    string credit = get_string("Number: ");

    if (strlen(credit) >= 5 && strlen(credit) <= 30)
    {
        //using luhnealgorethim to get the finalsum
        luhnealgorethim(credit);
    }
    else
    {
        do
        {
            credit = get_string("Number: ");
        }
        while (strlen(credit) < 15 || strlen(credit) > 17);
        luhnealgorethim(credit);
//asking the user to enter the right input
    }

    if (iscredit(luhnealgorethim(credit)) == true)
    {
        printf("%s", CreditType(credit));
    }
    else
    {
        printf("INVALID\n");
    }


}
int luhnealgorethim(string credit)
{
    int upperbound = strlen(credit);
    int nums[upperbound];
    int k = 0;
    int l = 1;
    int j = 0;
    int oddsum = 0;
    int finalsum = 0;
    //getting the input as a string and turning it to an integer
    for (int i = 0; i < upperbound ; i++)
    {
        nums[i] = credit[i] - '0';
    }
    //multiplying by 2
    while (k < upperbound )
    {
        nums[k] *= 2;
        k += 2;
    }
    while (j < upperbound )
    {

        if (nums[j] < 10)
        {
            oddsum = oddsum + nums[j];
        }
        else
        {
            //the sum of the product's digits
            int p = nums[j] % 10;
            int q = (nums[j] - p) / 10;
            oddsum += p + q;
        }
        j += 2;
    }
    while (l < upperbound)
    {
        //the final sum
        finalsum += nums[l];
        l += 2;
    }
    finalsum += oddsum;
    return finalsum;
    printf("finalsum is : %i", finalsum);
}
//method to check if the card is a credit or not
bool iscredit(int finalsum)
{

    if (finalsum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
//method to determine the credit's type
string CreditType(string credit)
{
    int nums[20];
    int long1 = strlen(credit);
    for (int z = 0; z < long1; z++)
    {
        nums[z] = credit[z] - '0';
    }
    //to get the first two numbers
    int firsttwo = (nums[0] * 10) + nums[1];
    if (long1 == 15 && (firsttwo == 34 || firsttwo == 37))
    {
        return "AMEX\n";
    }
    else if (long1 == 16 && (firsttwo == 51 || firsttwo == 52 || firsttwo == 53 || firsttwo == 54 || firsttwo == 55))
    {
        return "MASTERCARD\n";
    }
    else if ((long1 == 13 || long1 == 16) && nums[0] == 4)
    {
        return "VISA\n";
    }
    else
    {
        return "INVALID\n";
    }
}