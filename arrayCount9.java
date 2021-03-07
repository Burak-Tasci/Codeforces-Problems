import java.lang.reflect.Array;

public class arrayCount9 {

	public static void main(String[] args) {
		System.out.println(counts([1,9,7,9]));
	}
	
	static int counts(int[] nums)
	{
		int count = 0;
		
		for(int i = 0; i < nums.length;i++)
		{
			if((int)Array.get(nums,i) == 9)
			{
				count++;
			}
		}
		
		return count;
	}
}
