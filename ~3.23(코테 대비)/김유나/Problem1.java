import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ_13335_트럭 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int w = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());
		int time = 0;
		int weight = 0;
		
		st = new StringTokenizer(br.readLine());
		
		Queue<Integer> truck = new ArrayDeque<>();
		Queue<Integer> bridge = new ArrayDeque<>();
		
		for (int i = 0; i < n; i++) {
			truck.add(Integer.parseInt(st.nextToken()));
		}
		
		for (int i = 0; i < w; i++) {
			bridge.add(0);
		}
		
		while (!bridge.isEmpty()) {
			time++;
			weight -= bridge.poll();
			
			if (!truck.isEmpty()) {
				if (truck.peek() + weight <= L) {
					weight += truck.peek();
					bridge.add(truck.poll());
				} else {
					bridge.add(0);
				}
			}
		}
		
		System.out.print(time);
	}

}
