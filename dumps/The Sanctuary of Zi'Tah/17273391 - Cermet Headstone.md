# 17273391 - Cermet Headstone

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | The Sanctuary of Zi'Tah (ID: 121) |
| Block Size       | 1052 bytes                        |
| Total Events     | 4                                 |
| References Count | 18                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [200](#event-200)     | 0x0001       |     39 |             10 |
| [201](#event-201)     | 0x0028       |     39 |             10 |
| [202](#event-202)     | 0x004F       |    868 |             91 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E49      |        7753 |
|       1 | 0x1E4A      |        7754 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0013      |          19 |
|       5 | 0x00E9      |         233 |
|       6 | 0x00C8      |         200 |
|       7 | 0x002D      |          45 |
|       8 | 0x000D      |          13 |
|       9 | 0x00F7      |         247 |
|      10 | 0x1E5C      |        7772 |
|      11 | 0x00B4      |         180 |
|      12 | 0x005A      |          90 |
|      13 | 0x0003      |           3 |
|      14 | 0x001E      |          30 |
|      15 | 0x00C9      |         201 |
|      16 | 0x0002      |           2 |
|      17 | 0x00D7      |         215 |

## String References

- **7753**: 6... A single fragment of light. The way in which it shines suggests that it is resonating with something...
- **7754**: Do you remove the $3? [Yes./No.]
- **7772**: The $3 begins to glow.

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

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 48 00 80 23 24 01   J........H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 26 00 03 01  .....%......&...
0020: 10 03 80 01 26 00 21 00                           ....&.!.        
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x48] [System] [7753*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=7754*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0026
  6: 0x001E [0x03] Work_Zone[1] = 1*
  7: 0x0023 [0x01] GOTO 0x0026

SUBROUTINE_0026:
  8: 0x0026 [0x21] END_EVENT
  9: 0x0027 [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          4A F0 FF FF 7F F8 FF FF          J.......
0030: 7F 48 00 80 23 24 01 80  02 80 02 80 25 02 00 10  .H..#$......%...
0040: 02 80 00 4D 00 03 01 10  03 80 01 4D 00 21 00     ...M.......M.!. 
```

#### Opcodes

```
  0: 0x0028 [0x4A] LocalPlayer looks at EventEntity
  1: 0x0031 [0x48] [System] [7753*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0035 [0x24] CREATE_DIALOG(message_id=7754*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x003C [0x25] WAIT_DIALOG_SELECT()
  5: 0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004D
  6: 0x0045 [0x03] Work_Zone[1] = 1*
  7: 0x004A [0x01] GOTO 0x004D

SUBROUTINE_004D:
  8: 0x004D [0x21] END_EVENT
  9: 0x004E [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x004F    |
| Data Size    | 868 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               42                 B
0050: 1A 85 01 46 01 38 04 80  27 10 F0 FF FF 7F 02 80  ...F.8..'.......
0060: F0 FF FF 7F 45 05 80 F0  FF FF 7F F0 FF FF 7F 6C  ....E..........l
0070: 69 74 31 02 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  it1..E..........
0080: 66 64 69 32 02 80 27 10  30 92 07 01 02 1C 07 80  fdi2..'.0.......
0090: 62 08 80 32 92 07 01 32  92 07 01 6D 61 69 6E 02  b..2...2...main.
00A0: 80 03 02 10 09 80 48 0A  80 23 62 08 80 32 92 07  ......H..#b..2..
00B0: 01 32 92 07 01 6D 61 69  31 02 80 1C 0B 80 2C 30  .2...mai1.....,0
00C0: 92 07 01 30 92 07 01 64  65 61 64 29 10 30 92 07  ...0...dead).0..
00D0: 01 03 1C 0C 80 62 0D 80  31 92 07 01 31 92 07 01  .....b..1...1...
00E0: 6D 61 69 6E 02 80 1C 0E  80 79 00 F0 FF FF 7F 31  main.....y.....1
00F0: 92 07 01 1C 07 80 1A 85  01 1C 0E 80 46 00 45 06  ............F.E.
0100: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 02 80 45  .........fdi2..E
0110: 0F 80 F0 FF FF 7F F0 FF  FF 7F 71 73 74 63 02 80  ..........qstc..
0120: 21 00 45 06 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  !.E..........fdi
0130: 30 02 80 55 06 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0..U..........fd
0140: 69 30 1B 45 06 80 F0 FF  FF 7F F0 FF FF 7F 66 64  i0.E..........fd
0150: 6F 30 02 80 55 06 80 F0  FF FF 7F F0 FF FF 7F 66  o0..U..........f
0160: 64 6F 30 1B 45 06 80 F0  FF FF 7F F0 FF FF 7F 66  do0.E..........f
0170: 64 69 31 02 80 55 06 80  F0 FF FF 7F F0 FF FF 7F  di1..U..........
0180: 66 64 69 31 1B 45 06 80  F0 FF FF 7F F0 FF FF 7F  fdi1.E..........
0190: 66 64 6F 31 02 80 55 06  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
01A0: 7F 66 64 6F 31 1B 45 0F  80 F0 FF FF 7F F0 FF FF  .fdo1.E.........
01B0: 7F 77 68 69 31 02 80 55  0F 80 F0 FF FF 7F F0 FF  .whi1..U........
01C0: FF 7F 77 68 69 31 1B 45  0F 80 F0 FF FF 7F F0 FF  ..whi1.E........
01D0: FF 7F 77 68 6F 31 02 80  55 0F 80 F0 FF FF 7F F0  ..who1..U.......
01E0: FF FF 7F 77 68 6F 31 1B  45 0F 80 F0 FF FF 7F F0  ...who1.E.......
01F0: FF FF 7F 77 68 6F 32 02  80 55 0F 80 F0 FF FF 7F  ...who2..U......
0200: F0 FF FF 7F 77 68 6F 32  1B 45 0F 80 F0 FF FF 7F  ....who2.E......
0210: F0 FF FF 7F 77 68 6F 33  02 80 55 0F 80 F0 FF FF  ....who3..U.....
0220: 7F F0 FF FF 7F 77 68 6F  33 1B 62 03 80 F0 FF FF  .....who3.b.....
0230: 7F F0 FF FF 7F 6D 61 69  6E 02 80 1C 07 80 45 06  .....main.....E.
0240: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 55  .........fdo1..U
0250: 06 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 1B 45  ..........fdo1.E
0260: 06 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
0270: 62 10 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 02  b..........main.
0280: 80 1C 0E 80 55 06 80 F0  FF FF 7F F0 FF FF 7F 66  ....U..........f
0290: 64 69 31 1B 45 06 80 F0  FF FF 7F F0 FF FF 7F 62  di1.E..........b
02A0: 6C 6F 6E 02 80 45 0F 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
02B0: 62 6C 6F 6E 02 80 1B 45  0F 80 F0 FF FF 7F F0 FF  blon...E........
02C0: FF 7F 77 68 69 30 02 80  55 0F 80 F0 FF FF 7F F0  ..whi0..U.......
02D0: FF FF 7F 77 68 69 30 1B  45 0F 80 F0 FF FF 7F F0  ...whi0.E.......
02E0: FF FF 7F 77 68 6F 30 02  80 55 0F 80 F0 FF FF 7F  ...who0..U......
02F0: F0 FF FF 7F 77 68 6F 30  1B 45 11 80 F0 FF FF 7F  ....who0.E......
0300: F0 FF FF 7F 65 66 6F 6E  02 80 55 11 80 F0 FF FF  ....efon..U.....
0310: 7F F0 FF FF 7F 65 66 6F  6E 1B 45 06 80 F0 FF FF  .....efon.E.....
0320: 7F F0 FF FF 7F 66 64 69  73 02 80 1B 45 06 80 F0  .....fdis...E...
0330: FF FF 7F F0 FF FF 7F 66  64 6F 73 02 80 55 06 80  .......fdos..U..
0340: F0 FF FF 7F F0 FF FF 7F  66 64 6F 73 1B 45 06 80  ........fdos.E..
0350: F0 FF FF 7F F0 FF FF 7F  66 64 69 66 02 80 1B 45  ........fdif...E
0360: 06 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 66 02 80  ..........fdof..
0370: 55 06 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 66 1B  U..........fdof.
0380: 45 06 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 70 02  E..........fdip.
0390: 80 1B 45 06 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
03A0: 70 02 80 55 06 80 F0 FF  FF 7F F0 FF FF 7F 66 64  p..U..........fd
03B0: 6F 70 1B                                          op.             
```

#### Opcodes

```
  0: 0x004F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0050 [0x1A] CALL_SUBROUTINE(address=0x0185)
  2: 0x0053 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0055 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  4: 0x0058 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  5: 0x005F [0x80] LOAD_WAIT(entity=LocalPlayer)
  6: 0x0064 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "lit1" with entities [LocalPlayer, LocalPlayer], work=[233*, 0*]
  7: 0x0075 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0086 [0x27] REQ_SET(priority=0x10, entity_id=ScenarioBoss (ID: 17273392/0x01079230), tag_num=0x02)
  9: 0x008D [0x1C] WAIT(45* ticks)
 10: 0x0090 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Unnamed NPC (ID: 17273394/0x01079232), Unnamed NPC (ID: 17273394/0x01079232)], work=[13*, 0*]
 11: 0x00A1 [0x03] Work_Zone[2] = 247*
 12: 0x00A6 [0x48] [System] [7772*]:
    → "The $3 begins to glow."
 13: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00AA [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "mai1" with entities [Unnamed NPC (ID: 17273394/0x01079232), Unnamed NPC (ID: 17273394/0x01079232)], work=[13*, 0*]
 15: 0x00BB [0x1C] WAIT(180* ticks)
 16: 0x00BE [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [ScenarioBoss (ID: 17273392/0x01079230), ScenarioBoss (ID: 17273392/0x01079230)]
 17: 0x00CB [0x29] REQ_SET_WAIT(priority=0x10, entity_id=ScenarioBoss (ID: 17273392/0x01079230), tag_num=0x03)
 18: 0x00D2 [0x1C] WAIT(90* ticks)
 19: 0x00D5 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Unnamed NPC (ID: 17273393/0x01079231), Unnamed NPC (ID: 17273393/0x01079231)], work=[3*, 0*]
 20: 0x00E6 [0x1C] WAIT(30* ticks)
 21: 0x00E9 [0x79] LocalPlayer looks at Unnamed NPC (ID: 17273393/0x01079231) (Basic look)
 22: 0x00F3 [0x1C] WAIT(45* ticks)
 23: 0x00F6 [0x1A] CALL_SUBROUTINE(address=0x0185)
 24: 0x00F9 [0x1C] WAIT(30* ticks)
 25: 0x00FC [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x010F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 28: 0x0120 [0x21] END_EVENT
 29: 0x0121 [0x00] END_REQSTACK()

SUBROUTINE_0185:
 30: 0x0185 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x0196 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 32: 0x01A5 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0122 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0133 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0142 [0x1B] RETURN
     0x0143 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0154 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0163 [0x1B] RETURN
     0x0164 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0175 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0184 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x01A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01B7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01C6 [0x1B] RETURN
     0x01C7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01D8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01E7 [0x1B] RETURN
     0x01E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01F9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0208 [0x1B] RETURN
     0x0209 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x021A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0229 [0x1B] RETURN
     0x022A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x023B [0x1C] WAIT(45* ticks)
     0x023E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x024F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x025E [0x1B] RETURN
     0x025F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0270 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x0281 [0x1C] WAIT(30* ticks)
     0x0284 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0293 [0x1B] RETURN
     0x0294 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02B6 [0x1B] RETURN
     0x02B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02C8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02D7 [0x1B] RETURN
     0x02D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02E9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02F8 [0x1B] RETURN
     0x02F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x030A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0319 [0x1B] RETURN
     0x031A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x032B [0x1B] RETURN
     0x032C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x033D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x034C [0x1B] RETURN
     0x034D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x035E [0x1B] RETURN
     0x035F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0370 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x037F [0x1B] RETURN
     0x0380 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0391 [0x1B] RETURN
     0x0392 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03A3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03B2 [0x1B] RETURN
```
