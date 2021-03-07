
public class frontTimes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(rontTimes("Burak",3));
	}
	static String rontTimes(String str, int time)
	{
		String new_str = "";
		if(str.length() < 3)
		{
			while(time >0)
			{
				new_str += str;
				time--;
			}
		}
		else
		{
			while(time >0)
			{
				new_str += str.substring(0,3);
				time--;
			}
		}
		return new_str;
	}
}
