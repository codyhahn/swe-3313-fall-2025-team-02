import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        boolean isUser = isUser();
        boolean isAdmin = isAdmin();

        String rule;

        if (!isUser && !isAdmin) {
            rule = "R1"; // This is Guest
        } else if (isUser && !isAdmin) {
            rule = "R2"; // This is User
        } else if (isUser && isAdmin) {
            rule = "R3"; // This is Admin (inherits User rights)
        } else {
            return;
        }

        System.out.println("\nApplying Rule: " + rule);
        System.out.println("==============================");

        System.out.println("Self-Register:-------------- " + canSelfRegister(rule));
        System.out.println("Login:----------------------- " + canLogin(rule));
        System.out.println("View Inventory:-------------- " + canViewInventory(rule));
        System.out.println("Search Inventory:------------ " + canSearchInventory(rule));
        System.out.println("Purchase Items:-------------- " + canPurchaseItems(rule));
        System.out.println("Export Sales:---------------- " + canExportSales(rule));
        System.out.println("Run Reports:----------------- " + canRunReports(rule));
        System.out.println("Manage Inventory:------------ " + canManageInventory(rule));
    }

    static boolean isUser() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Is the person a User? (y/n): ");
        return sc.nextLine().equalsIgnoreCase("y");
    }

    static boolean isAdmin() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Is the person an Admin? (y/n): ");
        return sc.nextLine().equalsIgnoreCase("y");
    }

    // ACTION RULES
    // R1 = Guest (F,F)
    // R2 = User  (T,F)
    // R3 = Admin+User (T,T)

    static boolean canSelfRegister(String rule) {
        switch (rule) {
            case "R1": return true;
            case "R2":
            case "R3": return false;
            default: return false;
        }
    }

    static boolean canLogin(String rule) {
        switch (rule) {
            case "R1": return false;
            case "R2":
            case "R3": return true;
            default: return false;
        }
    }

    static boolean canViewInventory(String rule) {
        switch (rule) {
            case "R1": return false;
            case "R2":
            case "R3": return true;
            default: return false;
        }
    }

    static boolean canSearchInventory(String rule) {
        switch (rule) {
            case "R1": return false;
            case "R2":
            case "R3": return true;
            default: return false;
        }
    }

    static boolean canPurchaseItems(String rule) {
        switch (rule) {
            case "R1": return false;
            case "R2": return true;
            case "R3": return true;  // Admin can also purchase
            default: return false;
        }
    }

    static boolean canExportSales(String rule) {
        switch (rule) {
            case "R3": return true;  // Admin only
            default: return false;
        }
    }

    static boolean canRunReports(String rule) {
        switch (rule) {
            case "R3": return true;  // Admin only
            default: return false;
        }
    }

    static boolean canManageInventory(String rule) {
        switch (rule) {
            case "R3": return true; // Admin only
            default: return false;
        }
    }
}
