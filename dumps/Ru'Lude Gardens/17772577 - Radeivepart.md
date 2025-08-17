# 17772577 - Radeivepart

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 508 bytes                 |
| Total Events     | 5                         |
| References Count | 23                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [159](#event-159)     | 0x0001       |    262 |             54 |
| [61](#event-61)       | 0x0107       |     56 |             13 |
| [160](#event-160)     | 0x013F       |     58 |             18 |
| [10244](#event-10244) | 0x0179       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001E      |          30 |
|       2 | 0x280B      |       10251 |
|       3 | 0x280C      |       10252 |
|       4 | 0x280D      |       10253 |
|       5 | 0x003C      |          60 |
|       6 | 0x0001      |           1 |
|       7 | 0x019C      |         412 |
|       8 | 0x280E      |       10254 |
|       9 | 0x280F      |       10255 |
|      10 | 0x408A      |       16522 |
|      11 | 0x2810      |       10256 |
|      12 | 0x2811      |       10257 |
|      13 | 0x40000000  |  1073741824 |
|      14 | 0x0002      |           2 |
|      15 | 0x2812      |       10258 |
|      16 | 0x0003      |           3 |
|      17 | 0x2814      |       10260 |
|      18 | 0x2813      |       10259 |
|      19 | 0x00C9      |         201 |
|      20 | 0x2817      |       10263 |
|      21 | 0x2702      |        9986 |
|      22 | 0x2703      |        9987 |

## String References

- **9986**: The petition is now complete.
- **9987**: You have $0 more [signature/signatures] to go.
- **10251**: This monument was built at the end of the war...as a reminder that nobody should suffer like that ever again.
- **10252**: And now, people forget the mistakes of the past and quarrel all over again. I bet this is the only place where that promise is still remembered.
- **10253**: I want somebody to take this map I got in the north and stave off impending disaster, but you don't look ready for such a task.
- **10254**: Maybe you can take this $3 I got in the north, and stave off impending disaster... Do you think you've got what it takes?
- **10255**: What do you say? [I can do it./Not now.]
- **10256**: I knew you were the one! Now bring me $2 and show me what you're made of!
- **10257**: Well, that's a bummer. I thought you just might be the one!
- **10258**: Bring me $2. I'm counting on you!
- **10259**: Good job! I knew you could do it. But be on your guard.
- **10260**: Don't forget our vow here. Remember how precious peace is.
- **10263**: Well, if they can tear down the clock tower, who knows what they'll do to the monument? Quick, where do I sign?

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

### Event 159

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 262 bytes |
| Instructions | 54        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 76  F8 FF FF 7F 06 01 10 02   .....ov........
0010: 02 10 00 80 80 3D 00 5B  01 80 F8 FF FF 7F F8 FF  .....=.[........
0020: FF 7F 74 6C 6B 30 1D 02  80 23 1D 03 80 23 1D 04  ..tlk0...#...#..
0030: 80 23 5E 69 64 6C 30 1C  05 80 01 05 01 02 02 10  .#^idl0.........
0040: 06 80 80 B4 00 42 03 03  10 07 80 5B 01 80 F8 FF  .....B.....[....
0050: FF 7F F8 FF FF 7F 74 68  6B 31 1D 08 80 23 24 09  ......thk1...#$.
0060: 80 06 80 00 80 25 02 00  10 00 80 00 8E 00 5B 01  .....%........[.
0070: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 03 04 10  .........thk2...
0080: 0A 80 1D 0B 80 23 03 01  10 06 80 01 B1 00 02 00  .....#..........
0090: 10 06 80 00 B1 00 5B 01  80 F8 FF FF 7F F8 FF FF  ......[.........
00A0: 7F 74 68 6B 32 1D 0C 80  23 03 01 10 0D 80 01 B1  .thk2...#.......
00B0: 00 01 05 01 02 02 10 0E  80 80 DF 00 03 04 10 0A  ................
00C0: 80 5B 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .[..........tlk0
00D0: 1D 0F 80 23 5E 69 64 6C  30 1C 05 80 01 05 01 02  ...#^idl0.......
00E0: 02 10 10 80 80 05 01 5B  01 80 F8 FF FF 7F F8 FF  .......[........
00F0: FF 7F 74 6C 6B 30 1D 11  80 23 5E 69 64 6C 30 1C  ..tlk0...#^idl0.
0100: 05 80 01 05 01 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x000C [0x06] Work_Zone[1] = 0
  4: 0x000F [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x003D
  5: 0x0017 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=10251*)
    → "This monument was built at the end of the war...as a reminder that nobody should suffer like that ever again."
  7: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=10252*)
    → "And now, people forget the mistakes of the past and quarrel all over again. I bet this is the only place where that promise is still remembered."
  9: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=10253*)
    → "I want somebody to take this map I got in the north and stave off impending disaster, but you don't look ready for such a task."
 11: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0032 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x0037 [0x1C] WAIT(60* ticks)
 14: 0x003A [0x01] GOTO 0x0105
 15: 0x003D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x00B4
 16: 0x0045 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 17: 0x0046 [0x03] Work_Zone[3] = 412*
 18: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
 19: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=10254*)
    → "Maybe you can take this $3 I got in the north, and stave off impending disaster... Do you think you've got what it takes?"
 20: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x005E [0x24] CREATE_DIALOG(message_id=10255*, default_option=1*, option_flags=0*)
    → "What do you say? [I can do it./Not now.]"
 22: 0x0065 [0x25] WAIT_DIALOG_SELECT()
 23: 0x0066 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x008E
 24: 0x006E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
 25: 0x007D [0x03] Work_Zone[4] = 16522*
 26: 0x0082 [0x1D] PRINT_EVENT_MESSAGE(message_id=10256*)
    → "I knew you were the one! Now bring me $2 and show me what you're made of!"
 27: 0x0085 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0086 [0x03] Work_Zone[1] = 1*
 29: 0x008B [0x01] GOTO 0x00B1
 30: 0x008E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00B1
 31: 0x0096 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
 32: 0x00A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=10257*)
    → "Well, that's a bummer. I thought you just might be the one!"
 33: 0x00A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x00A9 [0x03] Work_Zone[1] = 1073741824*
 35: 0x00AE [0x01] GOTO 0x00B1

SUBROUTINE_00B1:
 36: 0x00B1 [0x01] GOTO 0x0105
 37: 0x00B4 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x00DF
 38: 0x00BC [0x03] Work_Zone[4] = 16522*
 39: 0x00C1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 40: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10258*)
    → "Bring me $2. I'm counting on you!"
 41: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00D4 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 43: 0x00D9 [0x1C] WAIT(60* ticks)
 44: 0x00DC [0x01] GOTO 0x0105
 45: 0x00DF [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0105
 46: 0x00E7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 47: 0x00F6 [0x1D] PRINT_EVENT_MESSAGE(message_id=10260*)
    → "Don't forget our vow here. Remember how precious peace is."
 48: 0x00F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x00FA [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 50: 0x00FF [0x1C] WAIT(60* ticks)
 51: 0x0102 [0x01] GOTO 0x0105

SUBROUTINE_0105:
 52: 0x0105 [0x21] END_EVENT
 53: 0x0106 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0107   |
| Data Size    | 56 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      20  01 42 1E F0 FF FF 7F 6F          .B.....o
0110: 70 5B 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  p[..........tlk0
0120: 1D 12 80 23 5E 69 64 6C  30 45 13 80 F0 FF FF 7F  ...#^idl0E......
0130: F0 FF FF 7F 71 73 74 63  00 80 1C 05 80 21 00     ....qstc.....!. 
```

#### Opcodes

```
  0: 0x0107 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0109 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x010A [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x010F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0110 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0111 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x0120 [0x1D] PRINT_EVENT_MESSAGE(message_id=10259*)
    → "Good job! I knew you could do it. But be on your guard."
  7: 0x0123 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0124 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0129 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x013A [0x1C] WAIT(60* ticks)
 11: 0x013D [0x21] END_EVENT
 12: 0x013E [0x00] END_REQSTACK()
```

### Event 160

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 58 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               20                  
0140: 01 42 1E F0 FF FF 7F 6F  70 5B 01 80 F8 FF FF 7F  .B.....op[......
0150: F8 FF FF 7F 74 6C 6B 30  1D 14 80 23 02 02 10 00  ....tlk0...#....
0160: 80 00 6B 01 48 15 80 23  01 6F 01 48 16 80 23 5E  ..k.H..#.o.H..#^
0170: 69 64 6C 30 1C 05 80 21  00                       idl0...!.       
```

#### Opcodes

```
  0: 0x013F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0141 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0142 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0147 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0148 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0149 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  6: 0x0158 [0x1D] PRINT_EVENT_MESSAGE(message_id=10263*)
    → "Well, if they can tear down the clock tower, who knows what they'll do to the monument? Quick, where do I sign?"
  7: 0x015B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x015C [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x016B
  9: 0x0164 [0x48] [System] [9986*]:
    → "The petition is now complete."
 10: 0x0167 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0168 [0x01] GOTO 0x016F
 12: 0x016B [0x48] [System] [9987*]:
    → "You have $0 more [signature/signatures] to go."
 13: 0x016E [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_016F:
 14: 0x016F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 15: 0x0174 [0x1C] WAIT(60* ticks)
 16: 0x0177 [0x21] END_EVENT
 17: 0x0178 [0x00] END_REQSTACK()
```

### Event 10244

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0179  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             00                             .      
```

#### Opcodes

```
  0: 0x0179 [0x00] END_REQSTACK()
```
