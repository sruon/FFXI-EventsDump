# 17818231 - Ranpi-Monpi

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 664 bytes                    |
| Total Events     | 5                            |
| References Count | 32                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [224](#event-224)     | 0x0001       |    231 |             54 |
| [225](#event-225)     | 0x00E8       |     41 |             13 |
| [229](#event-229)     | 0x0111       |    198 |             38 |
| [230](#event-230)     | 0x01D7       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001E      |          30 |
|       2 | 0x0028      |          40 |
|       3 | 0x1F01      |        7937 |
|       4 | 0x1F02      |        7938 |
|       5 | 0x0001      |           1 |
|       6 | 0x1F03      |        7939 |
|       7 | 0x1F04      |        7940 |
|       8 | 0x1F05      |        7941 |
|       9 | 0x1F06      |        7942 |
|      10 | 0x1F07      |        7943 |
|      11 | 0x1F08      |        7944 |
|      12 | 0x1F09      |        7945 |
|      13 | 0x1F0A      |        7946 |
|      14 | 0x1F0B      |        7947 |
|      15 | 0x1F17      |        7959 |
|      16 | 0x1F18      |        7960 |
|      17 | 0x1F19      |        7961 |
|      18 | 0x1F1A      |        7962 |
|      19 | 0x1F0C      |        7948 |
|      20 | 0x1F0E      |        7950 |
|      21 | 0x1F0F      |        7951 |
|      22 | 0x1F10      |        7952 |
|      23 | 0x1F11      |        7953 |
|      24 | 0x0002      |           2 |
|      25 | 0x1F12      |        7954 |
|      26 | 0x0003      |           3 |
|      27 | 0x1F13      |        7955 |
|      28 | 0x1F14      |        7956 |
|      29 | 0x1F15      |        7957 |
|      30 | 0x1F16      |        7958 |
|      31 | 0x00C9      |         201 |

## String References

- **7937**: Ah, vous over zere! Oui, vous! Are vous quick on vos feet?
- **7938**: Are vous quick on vos feet? [Mais oui!/Non...]
- **7939**: Eez zhat so... Zen I have no use for vous. Away with vous.
- **7940**: Dieu merci! I have awaited zee coming of une such as vous!
- **7941**: Allow moi to explain zee situation.
- **7942**: Zee area beyond is zee nesting grounds for wivre, vous see, wizeen wheech wivre eggs--une tres riche source de nutrition--can be found.
- **7943**: Eet eez known zat he who feasts on wivre egg cuisine gains zee vitalit<Player>i of ten tigres. For zee sake of zee survivors, such a valuable resource cannot be left unharnessed! Hoh-hoh-hoh!
- **7944**: For zis raison, I require for vous to procure an egg for moi.
- **7945**: Be duly warned, however, zat zee eggs are extremement fragile, and will not long wizstand duress from zee enemy.
- **7946**: So fragile are zhey, een fact, zhey are even known to crack wizeen zee hands of personnes een poor healz!
- **7947**: And don't even zink of taking zem zroo zee veridical confluxes, for zhey will not survive the grueling voyage intact!
- **7948**: I require for vous to procure a wivre egg from zees nesting grounds beyond.
- **7950**: Ah, vous have brought moi zee egg I requested! Merci beaucoup!
- **7951**: Sacre bleu! Why, zis egg eez cracked terriblement!
- **7952**: <Sigh> Zis places severe limitations upon mes options culinaires... Next time, vous must take care to bring the egg intact. Compris?
- **7953**: Ah, zee characteristic, inviting warmz of zee wivre egg...
- **7954**: Ah, zis toasty warmz radiating forz from zee egg...
- **7955**: Ah, zis irr<Player>ipressible warmz zat permeates to zee very core of mon being!
- **7956**: Wiz such un beau sp<Player>icimen, a delectable dish will surely be born zis day! Hoh-hoh-hoh!
- **7957**: Please accept zis as un petit token of mon gratitude.
- **7958**: I should appreciate help from vous again in the future! Till zen, bon voyage, mon ami!
- **7959**: Salut! Have vous come to again procure a wivre egg for moi?
- **7960**: Bring Ranpi-Monpi a wivre egg? [Mais oui!/Non...]
- **7961**: Eez zhat so... Well zen, perhaps anozer time.
- **7962**: Merci beaucoup, mon ami! I await zee egg wiz bated brez!

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

### Event 224

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 231 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 01 10 00 80 1E  F0 FF FF 7F 1C 01 80 66   B.............f
0010: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 02 02  ..........tlk0..
0020: 10 00 80 00 93 00 1D 03  80 23 66 02 80 F8 FF FF  .........#f.....
0030: 7F F8 FF FF 7F 74 6C 6B  31 24 04 80 00 80 00 80  .....tlk1$......
0040: 25 02 00 10 05 80 00 61  00 66 02 80 F8 FF FF 7F  %......a.f......
0050: F8 FF FF 7F 74 6C 6B 30  1D 06 80 23 21 00 01 61  ....tlk0...#!..a
0060: 00 66 02 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
0070: 1D 07 80 23 1D 08 80 23  1D 09 80 23 1D 0A 80 23  ...#...#...#...#
0080: 1D 0B 80 23 1D 0C 80 23  1D 0D 80 23 1D 0E 80 23  ...#...#...#...#
0090: 01 E1 00 1D 0F 80 23 66  02 80 F8 FF FF 7F F8 FF  ......#f........
00A0: FF 7F 74 6C 6B 31 24 10  80 05 80 00 80 25 02 00  ..tlk1$......%..
00B0: 10 05 80 00 CE 00 66 02  80 F8 FF FF 7F F8 FF FF  ......f.........
00C0: 7F 74 6C 6B 30 1D 11 80  23 21 00 01 CE 00 66 02  .tlk0...#!....f.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 12 80  .........tlk0...
00E0: 23 03 01 10 05 80 21 00                           #.....!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] Work_Zone[1] = 0*
  2: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000C [0x1C] WAIT(30* ticks)
  4: 0x000F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x001E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0093
  6: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=7937*)
    → "Ah, vous over zere! Oui, vous! Are vous quick on vos feet?"
  7: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  9: 0x0039 [0x24] CREATE_DIALOG(message_id=7938*, default_option=0*, option_flags=0*)
    → "Are vous quick on vos feet? [Mais oui!/Non...]"
 10: 0x0040 [0x25] WAIT_DIALOG_SELECT()
 11: 0x0041 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0061
 12: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 13: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7939*)
    → "Eez zhat so... Zen I have no use for vous. Away with vous."
 14: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x005C [0x21] END_EVENT
 16: 0x005D [0x00] END_REQSTACK()

SUBROUTINE_0061:
 17: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 18: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=7940*)
    → "Dieu merci! I have awaited zee coming of une such as vous!"
 19: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=7941*)
    → "Allow moi to explain zee situation."
 21: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=7942*)
    → "Zee area beyond is zee nesting grounds for wivre, vous see, wizeen wheech wivre eggs--une tres riche source de nutrition--can be found."
 23: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=7943*)
    → "Eet eez known zat he who feasts on wivre egg cuisine gains zee vitalit<Player>i of ten tigres. For zee sake of zee survivors, such a valuable resource cannot be left unharnessed! Hoh-hoh-hoh!"
 25: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=7944*)
    → "For zis raison, I require for vous to procure an egg for moi."
 27: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7945*)
    → "Be duly warned, however, zat zee eggs are extremement fragile, and will not long wizstand duress from zee enemy."
 29: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7946*)
    → "So fragile are zhey, een fact, zhey are even known to crack wizeen zee hands of personnes een poor healz!"
 31: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7947*)
    → "And don't even zink of taking zem zroo zee veridical confluxes, for zhey will not survive the grueling voyage intact!"
 33: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0090 [0x01] GOTO 0x00E1
 35: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=7959*)
    → "Salut! Have vous come to again procure a wivre egg for moi?"
 36: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0097 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 38: 0x00A6 [0x24] CREATE_DIALOG(message_id=7960*, default_option=1*, option_flags=0*)
    → "Bring Ranpi-Monpi a wivre egg? [Mais oui!/Non...]"
 39: 0x00AD [0x25] WAIT_DIALOG_SELECT()
 40: 0x00AE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00CE
 41: 0x00B6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 42: 0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7961*)
    → "Eez zhat so... Well zen, perhaps anozer time."
 43: 0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00C9 [0x21] END_EVENT
 45: 0x00CA [0x00] END_REQSTACK()

SUBROUTINE_00CE:
 46: 0x00CE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
 47: 0x00DD [0x1D] PRINT_EVENT_MESSAGE(message_id=7962*)
    → "Merci beaucoup, mon ami! I await zee egg wiz bated brez!"
 48: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00E1:
 49: 0x00E1 [0x03] Work_Zone[1] = 1*
 50: 0x00E6 [0x21] END_EVENT
 51: 0x00E7 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x005E [0x01] GOTO 0x0061
# Dead code (unreachable instructions):
     0x00CB [0x01] GOTO 0x00CE
```

### Event 225

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E8   |
| Data Size    | 41 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          1E F0 FF FF 7F 1C 01 80          ........
00F0: 66 02 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0100: 13 80 23 1D 0C 80 23 1D  0D 80 23 1D 0E 80 23 21  ..#...#...#...#!
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x00E8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00ED [0x1C] WAIT(30* ticks)
  2: 0x00F0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=7948*)
    → "I require for vous to procure a wivre egg from zees nesting grounds beyond."
  4: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=7945*)
    → "Be duly warned, however, zat zee eggs are extremement fragile, and will not long wizstand duress from zee enemy."
  6: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0107 [0x1D] PRINT_EVENT_MESSAGE(message_id=7946*)
    → "So fragile are zhey, een fact, zhey are even known to crack wizeen zee hands of personnes een poor healz!"
  8: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x010B [0x1D] PRINT_EVENT_MESSAGE(message_id=7947*)
    → "And don't even zink of taking zem zroo zee veridical confluxes, for zhey will not survive the grueling voyage intact!"
 10: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x010F [0x21] END_EVENT
 12: 0x0110 [0x00] END_REQSTACK()
```

### Event 229

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0111    |
| Data Size    | 198 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    42 1E F0 FF FF 7F 1C  01 80 66 02 80 F8 FF FF   B........f.....
0120: 7F F8 FF FF 7F 74 6C 6B  30 1D 14 80 23 02 02 10  .....tlk0...#...
0130: 00 80 00 6D 01 66 02 80  F8 FF FF 7F F8 FF FF 7F  ...m.f..........
0140: 74 6C 6B 31 66 02 80 F8  FF FF 7F F8 FF FF 7F 67  tlk1f..........g
0150: 6B 72 30 1D 15 80 23 66  02 80 F8 FF FF 7F F8 FF  kr0...#f........
0160: FF 7F 67 6B 72 31 1D 16  80 23 01 C4 01 02 03 10  ..gkr1...#......
0170: 05 80 80 7C 01 1D 17 80  23 01 9A 01 02 03 10 18  ...|....#.......
0180: 80 80 8B 01 1D 19 80 23  01 9A 01 02 03 10 1A 80  .......#........
0190: 80 9A 01 1D 1B 80 23 01  9A 01 1D 1C 80 23 66 02  ......#......#f.
01A0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 66 02 80  .........tlk1f..
01B0: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 1D 1D 80 23  ........pas0...#
01C0: 1D 1E 80 23 45 1F 80 F0  FF FF 7F F0 FF FF 7F 71  ...#E..........q
01D0: 73 74 63 00 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x0111 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0112 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0117 [0x1C] WAIT(30* ticks)
  3: 0x011A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0129 [0x1D] PRINT_EVENT_MESSAGE(message_id=7950*)
    → "Ah, vous have brought moi zee egg I requested! Merci beaucoup!"
  5: 0x012C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x012D [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x016D
  7: 0x0135 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x0144 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=40*
  9: 0x0153 [0x1D] PRINT_EVENT_MESSAGE(message_id=7951*)
    → "Sacre bleu! Why, zis egg eez cracked terriblement!"
 10: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0157 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr1" with entities [EventEntity, EventEntity], work=40*
 12: 0x0166 [0x1D] PRINT_EVENT_MESSAGE(message_id=7952*)
    → "<Sigh> Zis places severe limitations upon mes options culinaires... Next time, vous must take care to bring the egg intact. Compris?"
 13: 0x0169 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x016A [0x01] GOTO 0x01C4
 15: 0x016D [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x017C
 16: 0x0175 [0x1D] PRINT_EVENT_MESSAGE(message_id=7953*)
    → "Ah, zee characteristic, inviting warmz of zee wivre egg..."
 17: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0179 [0x01] GOTO 0x019A
 19: 0x017C [0x02] IF !(Work_Zone[3] == 2*) GOTO 0x018B
 20: 0x0184 [0x1D] PRINT_EVENT_MESSAGE(message_id=7954*)
    → "Ah, zis toasty warmz radiating forz from zee egg..."
 21: 0x0187 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0188 [0x01] GOTO 0x019A
 23: 0x018B [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x019A
 24: 0x0193 [0x1D] PRINT_EVENT_MESSAGE(message_id=7955*)
    → "Ah, zis irr<Player>ipressible warmz zat permeates to zee very core of mon being!"
 25: 0x0196 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0197 [0x01] GOTO 0x019A

SUBROUTINE_019A:
 27: 0x019A [0x1D] PRINT_EVENT_MESSAGE(message_id=7956*)
    → "Wiz such un beau sp<Player>icimen, a delectable dish will surely be born zis day! Hoh-hoh-hoh!"
 28: 0x019D [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x019E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 30: 0x01AD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
 31: 0x01BC [0x1D] PRINT_EVENT_MESSAGE(message_id=7957*)
    → "Please accept zis as un petit token of mon gratitude."
 32: 0x01BF [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x01C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7958*)
    → "I should appreciate help from vous again in the future! Till zen, bon voyage, mon ami!"
 34: 0x01C3 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_01C4:
 35: 0x01C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 36: 0x01D5 [0x21] END_EVENT
 37: 0x01D6 [0x00] END_REQSTACK()
```

### Event 230

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D7   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                      1E  F0 FF FF 7F 1C 01 80 66         ........f
01E0: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 1E  ..........tlk0..
01F0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x01D7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01DC [0x1C] WAIT(30* ticks)
  2: 0x01DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x01EE [0x1D] PRINT_EVENT_MESSAGE(message_id=7958*)
    → "I should appreciate help from vous again in the future! Till zen, bon voyage, mon ami!"
  4: 0x01F1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01F2 [0x21] END_EVENT
  6: 0x01F3 [0x00] END_REQSTACK()
```
