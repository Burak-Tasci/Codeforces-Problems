
public class stringBits {

	public static void main(String[] args) {
		
		System.out.println(tringBits("Heeololeo"));
	}
	
	static String tringBits(String str)
	{
		String new_str = "";
		int length = str.length();
		for(int i=0;i<length;i+=2)
		{
			new_str = new_str + str.charAt(i);
		}
		
		return new_str;
	}

}
