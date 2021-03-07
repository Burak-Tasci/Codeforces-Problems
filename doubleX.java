
public class doubleX {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "xaxx";
		boolean bool = oubleX(str);
		System.out.println(bool);
	}
	
	static boolean oubleX(String str)
	{
		str = str.toLowerCase();
		int length =str.length();
		//System.out.println(length);
		for(int i = 0; i< length; i++)
		{
			if(i != length-1)
			{
				char f_char = str.charAt(i);
				char s_char = str.charAt(i+1);
				if(f_char == 'x')
				{
					if(f_char == 'x' && s_char == 'x')
					{
						return true;
					}
					else
					{
						return false;
					}
				}

			}
			else
			{
				return false;
			}
		}
		return false;
	}
	
}
