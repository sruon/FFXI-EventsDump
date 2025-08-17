# 17772564 - Crooked Arrow

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 548 bytes                 |
| Total Events     | 8                         |
| References Count | 17                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [14](#event-14)       | 0x0001       |     60 |             12 |
| [15](#event-15)       | 0x003D       |     56 |             10 |
| [16](#event-16)       | 0x0075       |     56 |             10 |
| [149](#event-149)     | 0x00AD       |    152 |             29 |
| [10090](#event-10090) | 0x0145       |     52 |             12 |
| [10272](#event-10272) | 0x0179       |     26 |              8 |
| [10273](#event-10273) | 0x0193       |     27 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0045      |          69 |
|       1 | 0x2B40      |       11072 |
|       2 | 0x2B41      |       11073 |
|       3 | 0x2B52      |       11090 |
|       4 | 0x2B5D      |       11101 |
|       5 | 0x27DC      |       10204 |
|       6 | 0x27DD      |       10205 |
|       7 | 0x0000      |           0 |
|       8 | 0x0001      |           1 |
|       9 | 0x27E0      |       10208 |
|      10 | 0x27E1      |       10209 |
|      11 | 0x27DE      |       10206 |
|      12 | 0x27DF      |       10207 |
|      13 | 0x3610      |       13840 |
|      14 | 0x001E      |          30 |
|      15 | 0x3613      |       13843 |
|      16 | 0x3614      |       13844 |

## String References

- **10204**: Say... You know Aldo, the guy who runs the organization called the Tenshodo?
- **10205**: Do you know him? [Yes./No.]
- **10206**: The Tenshodo was founded by Aldo's father. They've done so well in trading abroad that they own the black market in these parts. Er, so I've heard...
- **10207**: Aldo took over after his father died. I've heard all kinds of things about him, but they say he's a smart and honorable man.
- **10208**: Oh, you're a Tenshodo member? I guess you know more than I do, then.
- **10209**: You should do business with the Tenshodo, too. They supply us with hard-to-find goods now and then.
- **11072**: Did you know there is a mysterious group of officials in Jeuno known as the "Armathrwn Society"?
- **11073**: The last time I tried telling some of the new recruits about the group, Captain Wolfgang put me on latrine duty for nine and a half weeks!
- **11090**: Members of the Armathrwn Society are to accompany the armada on its mission. It is said that the society's technological advancements are what built this city and made it what it is today.
- **11101**: Even with the technology of the Armathrwn Society on our side, the armada was unable to completely defeat the Wyrmking and his army. Perhaps we underestimated their power...
- **13840**: <Player>'s badge flashes brightly.
- **13843**: I see you've got a Salaheem's Sentinel badge there... They must be desperate to use those as an attention-grabbing device.
- **13844**: Maybe the empress of Aht Urhgan is short on devoted subjects...

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

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=11072*)
    → "Did you know there is a mysterious group of officials in Jeuno known as the "Armathrwn Society"?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=11073*)
    → "The last time I tried telling some of the new recruits about the group, Captain Wolfgang put me on latrine duty for nine and a half weeks!"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
  9: 0x002E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 10: 0x003B [0x21] END_EVENT
 11: 0x003C [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1E F0 FF               ...
0040: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0050: 6C 6B 30 1D 03 80 23 66  00 80 F8 FF FF 7F F8 FF  lk0...#f........
0060: FF 7F 74 6C 6B 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk1S........t
0070: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x003D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0043 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0044 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  4: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=11090*)
    → "Members of the Armathrwn Society are to accompany the armada on its mission. It is said that the society's technological advancements are what built this city and made it what it is today."
  5: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0057 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
  7: 0x0066 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x0073 [0x21] END_EVENT
  9: 0x0074 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                1E F0 FF  FF 7F 6F 70 66 00 80 F8       .....opf...
0080: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 04 80 23 66  .......tlk0...#f
0090: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 53 F8  ..........tlk1S.
00A0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0075 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  4: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=11101*)
    → "Even with the technology of the Armathrwn Society on our side, the armada was unable to completely defeat the Wyrmking and his army. Perhaps we underestimated their power..."
  5: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
  7: 0x009E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x00AB [0x21] END_EVENT
  9: 0x00AC [0x00] END_REQSTACK()
```

### Event 149

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AD    |
| Data Size    | 152 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         1E F0 FF               ...
00B0: FF 7F 6F 76 F8 FF FF 7F  66 00 80 F8 FF FF 7F F8  ..ov....f.......
00C0: FF FF 7F 74 6C 6B 30 1D  05 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
00D0: 24 06 80 07 80 07 80 25  02 00 10 07 80 00 05 01  $......%........
00E0: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 02  f..........tlk0.
00F0: 02 10 08 80 00 FE 00 1D  09 80 23 01 02 01 1D 0A  ..........#.....
0100: 80 23 01 27 01 02 00 10  08 80 00 27 01 66 00 80  .#.'.......'.f..
0110: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 0B 80 23  ........tlk0...#
0120: 1D 0C 80 23 01 27 01 66  00 80 F8 FF FF 7F F8 FF  ...#.'.f........
0130: FF 7F 74 6C 6B 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..tlk1S........t
0140: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x00AD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B3 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x00B8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  4: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10204*)
    → "Say... You know Aldo, the guy who runs the organization called the Tenshodo?"
  5: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00CB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x00D0 [0x24] CREATE_DIALOG(message_id=10205*, default_option=0*, option_flags=0*)
    → "Do you know him? [Yes./No.]"
  8: 0x00D7 [0x25] WAIT_DIALOG_SELECT()
  9: 0x00D8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0105
 10: 0x00E0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
 11: 0x00EF [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x00FE
 12: 0x00F7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10208*)
    → "Oh, you're a Tenshodo member? I guess you know more than I do, then."
 13: 0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00FB [0x01] GOTO 0x0102
 15: 0x00FE [0x1D] PRINT_EVENT_MESSAGE(message_id=10209*)
    → "You should do business with the Tenshodo, too. They supply us with hard-to-find goods now and then."
 16: 0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0102:
 17: 0x0102 [0x01] GOTO 0x0127
 18: 0x0105 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0127
 19: 0x010D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
 20: 0x011C [0x1D] PRINT_EVENT_MESSAGE(message_id=10206*)
    → "The Tenshodo was founded by Aldo's father. They've done so well in trading abroad that they own the black market in these parts. Er, so I've heard..."
 21: 0x011F [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0120 [0x1D] PRINT_EVENT_MESSAGE(message_id=10207*)
    → "Aldo took over after his father died. I've heard all kinds of things about him, but they say he's a smart and honorable man."
 23: 0x0123 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0124 [0x01] GOTO 0x0127

SUBROUTINE_0127:
 25: 0x0127 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
 26: 0x0136 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 27: 0x0143 [0x21] END_EVENT
 28: 0x0144 [0x00] END_REQSTACK()
```

### Event 10090

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                42 48 0D  80 1E F0 FF FF 7F 1C 0E       BH.........
0150: 80 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
0160: 1D 0F 80 23 1D 10 80 23  66 00 80 F8 FF FF 7F F8  ...#...#f.......
0170: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x0145 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0146 [0x48] [System] [13840*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0149 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x014E [0x1C] WAIT(30* ticks)
  4: 0x0151 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  5: 0x0160 [0x1D] PRINT_EVENT_MESSAGE(message_id=13843*)
    → "I see you've got a Salaheem's Sentinel badge there... They must be desperate to use those as an attention-grabbing device."
  6: 0x0163 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0164 [0x1D] PRINT_EVENT_MESSAGE(message_id=13844*)
    → "Maybe the empress of Aht Urhgan is short on devoted subjects..."
  8: 0x0167 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0168 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
 10: 0x0177 [0x21] END_EVENT
 11: 0x0178 [0x00] END_REQSTACK()
```

### Event 10272

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0179   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             4A F8 FF FF 7F F0 FF           J......
0180: FF 7F 4A F0 FF FF 7F F8  FF FF 7F 6F 70 1D 05 10  ..J........op...
0190: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0179 [0x4A] EventEntity looks at LocalPlayer
  1: 0x0182 [0x4A] LocalPlayer looks at EventEntity
  2: 0x018B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x018C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x018D [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  5: 0x0190 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0191 [0x21] END_EVENT
  7: 0x0192 [0x00] END_REQSTACK()
```

### Event 10273

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0193   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:          42 4A F8 FF FF  7F F0 FF FF 7F 4A F0 FF     BJ........J..
01A0: FF 7F F8 FF FF 7F 6F 70  1D 05 10 23 21 00        ......op...#!.  
```

#### Opcodes

```
  0: 0x0193 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0194 [0x4A] EventEntity looks at LocalPlayer
  2: 0x019D [0x4A] LocalPlayer looks at EventEntity
  3: 0x01A6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01A7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x01A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  6: 0x01AB [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01AC [0x21] END_EVENT
  8: 0x01AD [0x00] END_REQSTACK()
```
