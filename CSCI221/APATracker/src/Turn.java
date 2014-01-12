public class Turn {
	// ATTRIBUTES
	private int PointsEarned;
	private int Counter = 1;
	
	// ********  METHODS  **********

	public Turn() {
		
		PointsEarned = 0;
		// TODO Remove when done testing
		// System.out.println("Points Earned: " + this.getPointsEarned());
	}
	
	
	// GETTERS and SETTERS
	public void setPointsEarned(int Points) {PointsEarned = Points;}
	public int getPointsEarned() {return PointsEarned; }
	public int getTurn() { return Counter; }
}