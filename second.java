// Project.java
// Kruskal's Algorithm with GUI (Java Swing version of Turbo C code)

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class second extends JFrame {
    private CardLayout cardLayout;
    private JPanel mainPanel;
    private JTextArea consoleOutput;

    private int[][] cost;
    private int[] parent;
    private int n;

    // Constructor
    public second() {
        setTitle("Kruskal's Algorithm Project");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        cardLayout = new CardLayout();
        mainPanel = new JPanel(cardLayout);

        // Intro screen
        JPanel introPanel = new JPanel() {
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                setBackground(Color.BLACK);
                g.setColor(Color.RED);
                g.setFont(new Font("Serif", Font.BOLD, 36));
                g.drawString("WELCOME TO", 250, 100);
                g.drawString("OUR PROJECT", 250, 160);

                g.setColor(Color.GREEN);
                g.setFont(new Font("Serif", Font.PLAIN, 20));
                g.drawString("SUBMITTED TO : MISS PRIYANKA GHAI", 200, 300);
                g.drawString("SUBMITTED BY : JADWINDER SINGH", 200, 340);
            }
        };
        introPanel.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                cardLayout.show(mainPanel, "menu");
            }
        });

        // Menu screen
        JPanel menuPanel = new JPanel() {
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                setBackground(Color.BLACK);
                g.setColor(Color.CYAN);
                g.setFont(new Font("Serif", Font.BOLD, 36));
                g.drawString("MENU", 330, 100);

                g.setFont(new Font("Serif", Font.PLAIN, 24));
                g.setColor(Color.YELLOW);
                g.drawString("1. NON-GRAPHICAL MODE", 200, 200);
                g.drawString("2. GRAPHICAL MODE", 200, 250);
                g.drawString("3. EXIT", 200, 300);
            }
        };
        menuPanel.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                int choice = Integer.parseInt(
                    JOptionPane.showInputDialog("Enter your choice:")
                );
                if (choice == 1) runNonGraphical();
                else if (choice == 2) cardLayout.show(mainPanel, "graph");
                else System.exit(0);
            }
        });

        // Graphical panel
        JPanel graphPanel = new GraphPanel();

        // Console Panel
        JPanel consolePanel = new JPanel(new BorderLayout());
        consoleOutput = new JTextArea();
        consoleOutput.setEditable(false);
        consolePanel.add(new JScrollPane(consoleOutput), BorderLayout.CENTER);

        // Add panels
        mainPanel.add(introPanel, "intro");
        mainPanel.add(menuPanel, "menu");
        mainPanel.add(graphPanel, "graph");
        mainPanel.add(consolePanel, "console");

        add(mainPanel);
        cardLayout.show(mainPanel, "intro");
    }

    // Non-graphical Kruskal
    private void runNonGraphical() {
        n = Integer.parseInt(JOptionPane.showInputDialog("Enter number of vertices:"));
        cost = new int[n + 1][n + 1];
        parent = new int[n + 1];

        consoleOutput.setText("Implementation of Kruskal's Algorithm\n");
        for (int i = 1; i <= n; i++) {
            String[] row = JOptionPane.showInputDialog(
                "Enter row " + i + " of adjacency matrix (space separated):"
            ).split(" ");
            for (int j = 1; j <= n; j++) {
                cost[i][j] = Integer.parseInt(row[j - 1]);
                if (cost[i][j] == 0) cost[i][j] = 999;
            }
        }

        int ne = 1, mincost = 0;
        while (ne < n) {
            int min = 999, a = -1, b = -1, u = -1, v = -1;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (cost[i][j] < min) {
                        min = cost[i][j];
                        a = u = i;
                        b = v = j;
                    }
                }
            }
            u = find(u);
            v = find(v);
            if (uni(u, v)) {
                consoleOutput.append(ne + " edge (" + a + "," + b + ") = " + min + "\n");
                ne++;
                mincost += min;
            }
            cost[a][b] = cost[b][a] = 999;
        }
        consoleOutput.append("Minimum cost = " + mincost + "\n");

        cardLayout.show(mainPanel, "console");
    }

    private int find(int i) {
        while (parent[i] != 0) i = parent[i];
        return i;
    }

    private boolean uni(int i, int j) {
        if (i != j) {
            parent[j] = i;
            return true;
        }
        return false;
    }

    // Graphical representation of Kruskal’s steps
    class GraphPanel extends JPanel {
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            setBackground(Color.BLACK);

            g.setColor(Color.YELLOW);
            g.setFont(new Font("Serif", Font.BOLD, 20));
            g.drawString("Graphical Mode (Demo Graph)", 220, 40);

            // Nodes
            int[][] coords = {
                {90, 90}, {150, 120}, {190, 170}, {150, 250}, {80, 220}, {35, 170}, {110, 170}
            };
            String[] labels = {"1", "2", "3", "4", "5", "6", "7"};

            for (int i = 0; i < coords.length; i++) {
                g.setColor(Color.CYAN);
                g.fillOval(coords[i][0] - 10, coords[i][1] - 10, 20, 20);
                g.setColor(Color.BLACK);
                g.drawString(labels[i], coords[i][0] - 4, coords[i][1] + 4);
            }

            // Example edges
            g.setColor(Color.WHITE);
            g.drawLine(90, 90, 150, 120); // 1-2
            g.drawString("28", 120, 95);

            g.drawLine(90, 90, 35, 170); // 1-6
            g.drawString("10", 60, 120);

            g.drawLine(150, 120, 190, 170); // 2-3
            g.drawString("16", 170, 135);

            g.drawLine(110, 170, 150, 120); // 7-2
            g.drawString("14", 120, 150);

            g.drawLine(110, 170, 150, 250); // 7-4
            g.drawString("18", 130, 200);

            g.drawLine(150, 250, 80, 220); // 4-5
            g.drawString("22", 110, 240);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Project().setVisible(true));
    }
}
