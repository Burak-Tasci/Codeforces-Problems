import java.util.Scanner;

public class Elephant {
	/*
	An elephant decided to visit his friend. 
	It turned out that the elephant's house is 
	located at point 0 and his friend's house is 
	located at point x(x > 0) of the coordinate line. 
	In one step the elephant can move 1, 2, 3, 4 or 5 
	positions forward. Determine, what is the minimum 
	number of steps he need to make in order to get to 
	his friend's house.
	*/
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		int way = scan.nextInt();
		scan.close();
		System.out.println(find_min_way(way));

		
		
	}
	static int find_min_way(int way)
	{
		int times = 0;
		
		if(way<=5)
		{
			times=1;
		}
		else
		{
			times = way / 5;
			if(way % 5 != 0)
			{
				times+=1;
			}
		}
		
		return times;
	}

}
