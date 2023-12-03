package undo;
public interface Command {
	public void execute();
	public void undo();
}
class NoCommand implements Command {
	public void execute ( ) { };
    public void undo() { };
}


