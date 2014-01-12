
public class BusinessAddress extends Address {

BusinessAddress(String inStreet, String inCity, String inState, String inZip, boolean inIsResidence)
	{
		super(inStreet,inCity,inState,inZip);
		isResidence = inIsResidence;
	}
	
	private boolean isResidence;

public boolean isResidence() {
	return isResidence;
}

public void setResidence(boolean isResidence) {
	this.isResidence = isResidence;
}
}
