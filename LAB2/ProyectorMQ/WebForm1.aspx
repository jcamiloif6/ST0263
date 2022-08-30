<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="ProyectorMQ.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            Seleccione Cola
            <br />
            <asp:DropDownList ID="DropDownList1" runat="server">
                <asp:ListItem>cola1</asp:ListItem>
                <asp:ListItem>cola2</asp:ListItem>
            </asp:DropDownList>
            <br />
            <br />
            Ingrese Temperatura

        </div>
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        Ingrese Humedad<br />
&nbsp;<asp:TextBox ID="TextBox2" runat="server" style="margin-bottom: 0px"></asp:TextBox>
        <br />
        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Enviar" />
    </form>
</body>
</html>
