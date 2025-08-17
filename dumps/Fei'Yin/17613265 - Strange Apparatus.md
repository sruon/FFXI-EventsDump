# 17613265 - Strange Apparatus

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 468 bytes         |
| Total Events     | 9                 |
| References Count | 24                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [32](#event-32)       | 0x0001       |    127 |             45 |
| [33](#event-33)       | 0x0080       |    184 |             42 |
| [34](#event-34)       | 0x0138       |      1 |              1 |
| [35](#event-35)       | 0x0139       |      1 |              1 |
| [36](#event-36)       | 0x013A       |      1 |              1 |
| [37](#event-37)       | 0x013B       |      1 |              1 |
| [38](#event-38)       | 0x013C       |      1 |              1 |
| [39](#event-39)       | 0x013D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D31      |        7473 |
|       1 | 0x2A27      |       10791 |
|       2 | 0x1D3A      |        7482 |
|       3 | 0x0002      |           2 |
|       4 | 0x2A28      |       10792 |
|       5 | 0x2A29      |       10793 |
|       6 | 0x0000      |           0 |
|       7 | 0x2A2A      |       10794 |
|       8 | 0x0001      |           1 |
|       9 | 0x2A2B      |       10795 |
|      10 | 0x2A2C      |       10796 |
|      11 | 0x2A2E      |       10798 |
|      12 | 0x05C2      |        1474 |
|      13 | 0x2A2F      |       10799 |
|      14 | 0x2A2D      |       10797 |
|      15 | 0x2A30      |       10800 |
|      16 | 0x1D3D      |        7485 |
|      17 | 0x2A31      |       10801 |
|      18 | 0x00B4      |         180 |
|      19 | 0x012C      |         300 |
|      20 | 0x2A32      |       10802 |
|      21 | 0x2A33      |       10803 |
|      22 | 0x2A35      |       10805 |
|      23 | 0x2A34      |       10804 |

## String References

- **7473**: It is some sort of device.
- **7482**: The voice of a young woman rings in your head.
- **7485**: The voice in your head has gone silent.
- **10791**: You can hear a faint metallic sound coming from the inside.
- **10792**: "Wel...to the Mount Emulato... Use of...devic...requires...registra...as administrator statu..."
- **10793**: "Those with...octor status can...nput a special passw...to regist...their ID as an administra..."
- **10794**: "Error. A searc...for your ID...not reveal administ...status..."
- **10795**: "Welc...octor <Player>..."
- **10796**: "...emulator...ill now conduc...administr...auth...zation. Please inp...your 8-digit passw..."
- **10797**: "Passw...error... You are not authoriz...to use this...progra..."
- **10798**: "Registr...n complete. Your access...evel is administrator."
- **10799**: "Initiat...Mount Emulat...program... You...able...use the...-E-G-A Melod..., a...chip and $0 to...ommenc...rocess..."
- **10800**: "Greetings, Administr...<Player>..."
- **10801**: "...commencin...final...rocess..."
- **10802**: "Succes...complet...the...process..."
- **10803**: "May the grac...of the wise...Altan...be with you...deliver...mercy...throug...divin...light..."
- **10804**: "gA critic...erro...has occurred in...decrypt...rocess... Exitin...rogram..."
- **10805**: "Successf...mpleted Moun...rocess... Test data...sent to...maste...ollectio...device..."

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 127 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 48 01 80  23 48 02 80 23 02 02 10   H..#H..#H..#...
0010: 03 80 01 1D 00 48 04 80  23 48 05 80 23 02 02 10  .....H..#H..#...
0020: 06 80 80 2C 00 48 07 80  23 01 7A 00 02 02 10 08  ...,.H..#.z.....
0030: 80 80 62 00 48 09 80 23  48 0A 80 23 71 00 71 01  ..b.H..#H..#q.q.
0040: 71 02 02 02 10 06 80 00  5B 00 42 48 0B 80 23 03  q.......[.BH..#.
0050: 02 10 0C 80 48 0D 80 23  01 5F 00 48 0E 80 23 01  ....H..#._.H..#.
0060: 7A 00 02 02 10 03 80 80  7A 00 48 0F 80 23 03 02  z.......z.H..#..
0070: 10 0C 80 48 0D 80 23 01  7A 00 48 10 80 23 21 00  ...H..#.z.H..#!.
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7473*]:
    → "It is some sort of device."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [10791*]:
    → "You can hear a faint metallic sound coming from the inside."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7482*]:
    → "The voice of a young woman rings in your head."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x001D
  7: 0x0015 [0x48] [System] [10792*]:
    → ""Wel...to the Mount Emulato... Use of...devic...requires...registra...as administrator statu...""
  8: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0019 [0x48] [System] [10793*]:
    → ""Those with...octor status can...nput a special passw...to regist...their ID as an administra...""
 10: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x001D [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x002C
 12: 0x0025 [0x48] [System] [10794*]:
    → ""Error. A searc...for your ID...not reveal administ...status...""
 13: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0029 [0x01] GOTO 0x007A
 15: 0x002C [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0062
 16: 0x0034 [0x48] [System] [10795*]:
    → ""Welc...octor <Player>...""
 17: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0038 [0x48] [System] [10796*]:
    → ""...emulator...ill now conduc...administr...auth...zation. Please inp...your 8-digit passw...""
 19: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x003C [0x71] USER_INPUT_HANDLER: Open password input dialog (sends packet 0x60)
 21: 0x003E [0x71] USER_INPUT_HANDLER: Check if player has input or exited
 22: 0x0040 [0x71] USER_INPUT_HANDLER: Check if server responded
 23: 0x0042 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x005B
 24: 0x004A [0x42] SET_CLI_EVENT_CANCEL_DATA()
 25: 0x004B [0x48] [System] [10798*]:
    → ""Registr...n complete. Your access...evel is administrator.""
 26: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x004F [0x03] Work_Zone[2] = 1474*
 28: 0x0054 [0x48] [System] [10799*]:
    → ""Initiat...Mount Emulat...program... You...able...use the...-E-G-A Melod..., a...chip and $0 to...ommenc...rocess...""
 29: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0058 [0x01] GOTO 0x005F
 31: 0x005B [0x48] [System] [10797*]:
    → ""Passw...error... You are not authoriz...to use this...progra...""
 32: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_005F:
 33: 0x005F [0x01] GOTO 0x007A
 34: 0x0062 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x007A
 35: 0x006A [0x48] [System] [10800*]:
    → ""Greetings, Administr...<Player>...""
 36: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x006E [0x03] Work_Zone[2] = 1474*
 38: 0x0073 [0x48] [System] [10799*]:
    → ""Initiat...Mount Emulat...program... You...able...use the...-E-G-A Melod..., a...chip and $0 to...ommenc...rocess...""
 39: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x0077 [0x01] GOTO 0x007A

SUBROUTINE_007A:
 41: 0x007A [0x48] [System] [7485*]:
    → "The voice in your head has gone silent."
 42: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x007E [0x21] END_EVENT
 44: 0x007F [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0080    |
| Data Size    | 184 bytes |
| Instructions | 42        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 42 4A F0 FF FF 7F F8 FF  FF 7F 02 02 10 03 80 00  BJ..............
0090: 96 00 48 00 80 23 48 02  80 23 2D D1 C1 0C 01 D1  ..H..#H..#-.....
00A0: C1 0C 01 6D 6E 74 72 2D  D1 C1 0C 01 D1 C1 0C 01  ...mntr-........
00B0: 6D 6F 6A 69 48 0F 80 23  02 02 10 06 80 80 EF 00  mojiH..#........
00C0: 48 11 80 23 2D D1 C1 0C  01 D1 C1 0C 01 69 74 69  H..#-........iti
00D0: 6E 1C 12 80 2D D1 C1 0C  01 D1 C1 0C 01 69 74 6F  n...-........ito
00E0: 74 1C 13 80 48 14 80 23  48 15 80 23 01 25 01 02  t...H..#H..#.%..
00F0: 02 10 08 80 80 FE 00 48  16 80 23 01 25 01 02 02  .......H..#.%...
0100: 10 03 80 80 0D 01 48 16  80 23 01 25 01 48 11 80  ......H..#.%.H..
0110: 23 2D D1 C1 0C 01 D1 C1  0C 01 69 74 69 6E 1C 12  #-........itin..
0120: 80 48 17 80 23 2D D1 C1  0C 01 D1 C1 0C 01 6B 69  .H..#-........ki
0130: 6C 6C 48 10 80 23 21 00                           llH..#!.        
```

#### Opcodes

```
  0: 0x0080 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0081 [0x4A] LocalPlayer looks at EventEntity
  2: 0x008A [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0096
  3: 0x0092 [0x48] [System] [7473*]:
    → "It is some sort of device."
  4: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0096 [0x48] [System] [7482*]:
    → "The voice of a young woman rings in your head."
  6: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009A [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "mntr" with entities [Strange Apparatus (ID: 17613265/0x010CC1D1), Strange Apparatus (ID: 17613265/0x010CC1D1)]
  8: 0x00A7 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "moji" with entities [Strange Apparatus (ID: 17613265/0x010CC1D1), Strange Apparatus (ID: 17613265/0x010CC1D1)]
  9: 0x00B4 [0x48] [System] [10800*]:
    → ""Greetings, Administr...<Player>...""
 10: 0x00B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00B8 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00EF
 12: 0x00C0 [0x48] [System] [10801*]:
    → ""...commencin...final...rocess...""
 13: 0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00C4 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "itin" with entities [Strange Apparatus (ID: 17613265/0x010CC1D1), Strange Apparatus (ID: 17613265/0x010CC1D1)]
 15: 0x00D1 [0x1C] WAIT(180* ticks)
 16: 0x00D4 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "itot" with entities [Strange Apparatus (ID: 17613265/0x010CC1D1), Strange Apparatus (ID: 17613265/0x010CC1D1)]
 17: 0x00E1 [0x1C] WAIT(300* ticks)
 18: 0x00E4 [0x48] [System] [10802*]:
    → ""Succes...complet...the...process...""
 19: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x00E8 [0x48] [System] [10803*]:
    → ""May the grac...of the wise...Altan...be with you...deliver...mercy...throug...divin...light...""
 21: 0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x00EC [0x01] GOTO 0x0125
 23: 0x00EF [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x00FE
 24: 0x00F7 [0x48] [System] [10805*]:
    → ""Successf...mpleted Moun...rocess... Test data...sent to...maste...ollectio...device...""
 25: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x00FB [0x01] GOTO 0x0125
 27: 0x00FE [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x010D
 28: 0x0106 [0x48] [System] [10805*]:
    → ""Successf...mpleted Moun...rocess... Test data...sent to...maste...ollectio...device...""
 29: 0x0109 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x010A [0x01] GOTO 0x0125
 31: 0x010D [0x48] [System] [10801*]:
    → ""...commencin...final...rocess...""
 32: 0x0110 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0111 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "itin" with entities [Strange Apparatus (ID: 17613265/0x010CC1D1), Strange Apparatus (ID: 17613265/0x010CC1D1)]
 34: 0x011E [0x1C] WAIT(180* ticks)
 35: 0x0121 [0x48] [System] [10804*]:
    → ""gA critic...erro...has occurred in...decrypt...rocess... Exitin...rogram...""
 36: 0x0124 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0125:
 37: 0x0125 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [Strange Apparatus (ID: 17613265/0x010CC1D1), Strange Apparatus (ID: 17613265/0x010CC1D1)]
 38: 0x0132 [0x48] [System] [7485*]:
    → "The voice in your head has gone silent."
 39: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x0136 [0x21] END_EVENT
 41: 0x0137 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0138  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          00                               .       
```

#### Opcodes

```
  0: 0x0138 [0x00] END_REQSTACK()
```

### Event 35

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0139  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             00                             .      
```

#### Opcodes

```
  0: 0x0139 [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                00                           .     
```

#### Opcodes

```
  0: 0x013A [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   00                         .    
```

#### Opcodes

```
  0: 0x013B [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                      00                       .   
```

#### Opcodes

```
  0: 0x013C [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         00                     .  
```

#### Opcodes

```
  0: 0x013D [0x00] END_REQSTACK()
```
