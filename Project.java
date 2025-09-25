import javax.swing.*;
import java.awt.*;
import java.util.*;

class Edge {
    int src, dest, weight;
    boolean chosen = false;
    boolean rejected = false;

    Edge(int s, int d, int w) { src = s; dest = d; weight = w; }
}

public class Project extends JFrame {
    private java.util.List<Edge> edges;
    private int step = 0;
    private GraphPanel originalGraph;
    private MSTPanel mstGraph;
    private JTextArea edgeListArea;
    private int[] parent;

    public Project() {
        setTitle("Kruskal Visualization");
        setSize(1100, 650);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Sample graph (7 nodes, weighted edges)
        edges = new ArrayList<>();
        edges.add(new Edge(1,6,10));
        edges.add(new Edge(3,4,12));
        edges.add(new Edge(2,7,14));
        edges.add(new Edge(4,7,18));
        edges.add(new Edge(5,7,24));
        edges.add(new Edge(4,5,22));
        edges.add(new Edge(2,3,16));
        edges.add(new Edge(1,2,28));
        edges.add(new Edge(5,6,25));

        Collections.sort(edges, Comparator.comparingInt(e -> e.weight));
        parent = new int[8]; // 1-based

        // Panels
        JPanel graphsPanel = new JPanel(new GridLayout(1, 2));
        originalGraph = new GraphPanel(edges, false, "Original Graph");
        mstGraph = new MSTPanel(edges, "MST Construction");
        graphsPanel.add(originalGraph);
        graphsPanel.add(mstGraph);

        edgeListArea = new JTextArea(6, 40);
        edgeListArea.setEditable(false);
        edgeListArea.setFont(new Font("Monospaced", Font.PLAIN, 14));
        JScrollPane scrollPane = new JScrollPane(edgeListArea);

        add(graphsPanel, BorderLayout.CENTER);
        add(scrollPane, BorderLayout.SOUTH);

        // Timer to animate
        new javax.swing.Timer(2500, e -> nextStep()).start();
    }

    private void nextStep() {
        if (step >= edges.size()) return;
        Edge edge = edges.get(step);
        int u = find(edge.src), v = find(edge.dest);
        if (u != v) {
            union(u, v);
            edge.chosen = true;
            edgeListArea.append("Chosen   : ("+edge.src+","+edge.dest+") w="+edge.weight+"\n");
        } else {
            edge.rejected = true;
            edgeListArea.append("Rejected : ("+edge.src+","+edge.dest+") w="+edge.weight+"\n");
        }
        edgeListArea.setCaretPosition(edgeListArea.getDocument().getLength()); // auto-scroll
        originalGraph.repaint();
        mstGraph.repaint();
        step++;
    }

    private int find(int i) {
        if (parent[i] == 0) return i;
        return parent[i] = find(parent[i]);
    }

    private void union(int i, int j) { parent[find(i)] = find(j); }

    // Panel for graph
    class GraphPanel extends JPanel {
        java.util.List<Edge> edges;
        boolean onlyMST;
        String title;

        // prettier node positions
        int[][] coords = {
            {0,0}, {150,80}, {350,80}, {500,180},
            {350,300}, {150,300}, {50,180}, {250,180}
        };

        GraphPanel(java.util.List<Edge> e, boolean mst, String title) {
            this.edges = e;
            this.onlyMST = mst;
            this.title = title;
            setPreferredSize(new Dimension(550, 550));
            setBackground(Color.BLACK);
        }

        protected void paintComponent(Graphics g) {
            super.paintComponent(g);

            Graphics2D g2 = (Graphics2D) g;
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            // Title
            g2.setColor(Color.YELLOW);
            g2.setFont(new Font("Arial", Font.BOLD, 18));
            g2.drawString(title, getWidth()/2 - 60, 25);

            // Draw edges
            g2.setFont(new Font("Arial", Font.PLAIN, 12));
            for (Edge ed : edges) {
                if (onlyMST && !ed.chosen) continue;
                int x1 = coords[ed.src][0], y1 = coords[ed.src][1];
                int x2 = coords[ed.dest][0], y2 = coords[ed.dest][1];

                if (ed.chosen) g2.setColor(Color.GREEN);
                else if (ed.rejected) g2.setColor(Color.RED);
                else g2.setColor(Color.LIGHT_GRAY);

                g2.setStroke(new BasicStroke(ed.chosen ? 3 : 1));
                g2.drawLine(x1, y1, x2, y2);

                // weight
                g2.setColor(Color.WHITE);
                g2.drawString(""+ed.weight, (x1+x2)/2, (y1+y2)/2);
            }

            // Draw nodes
            for (int i=1; i<=7; i++) {
                int x = coords[i][0], y = coords[i][1];
                g2.setColor(Color.CYAN);
                g2.fillOval(x-20, y-20, 40, 40);
                g2.setColor(Color.BLACK);
                g2.setFont(new Font("Arial", Font.BOLD, 14));
                g2.drawString(""+i, x-5, y+5);
            }
        }
    }

    // MST panel = only chosen edges
    class MSTPanel extends GraphPanel {
        MSTPanel(java.util.List<Edge> e, String title) { super(e, true, title); }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Project().setVisible(true));
    }
}
