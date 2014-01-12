import java.io.Serializable;


public class HomeAddress extends Address implements Serializable {
private String aptNo;

HomeAddress() {}
HomeAddress(String inStreet, String inCity, String inState, String inZip, String inAptNo)
{
	super(inStreet,inCity,inState,inZip);
	aptNo = inAptNo;
}


public String getAptNo() {
	return aptNo;
}

public void setAptNo(String aptNo) {
	this.aptNo = aptNo;
}
}
