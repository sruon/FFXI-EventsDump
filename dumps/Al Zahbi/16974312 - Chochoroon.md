# 16974312 - Chochoroon

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 296 bytes         |
| Total Events     | 4                 |
| References Count | 14                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [206](#event-206)     | 0x0001       |     52 |             13 |
| [260](#event-260)     | 0x0035       |    100 |             25 |
| [261](#event-261)     | 0x0099       |     52 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1DEE      |        7662 |
|       2 | 0x034A      |         842 |
|       3 | 0x1F03      |        7939 |
|       4 | 0x1F04      |        7940 |
|       5 | 0x0000      |           0 |
|       6 | 0x1F05      |        7941 |
|       7 | 0x1F06      |        7942 |
|       8 | 0x1F07      |        7943 |
|       9 | 0x0002      |           2 |
|      10 | 0x1F08      |        7944 |
|      11 | 0x1F09      |        7945 |
|      12 | 0x1F0A      |        7946 |
|      13 | 0x1F0B      |        7947 |

## String References

- **7662**: Nice adventooorer save Chochoroon, yes? Chochoroon very happy. Chochoroon give yooo present.
- **7939**: Chochoroon is appraiser, no? Yooo give Chochoroon item for appraisal, no? Chochoroon appraise for just $0 clink clink!
- **7940**: Appraise? [Appraise, yes?/Appraise, no!/Appraise...what?]
- **7941**: Appraise, okay? Chochoroon tell yooo mysterious item name for $0 gil, okay?
- **7942**: Chochoroon put item with your treasooor, okay? So leave rooom, okay? And make sure can have more than one of item, yes?
- **7943**: Appraise, no? Bye bye, okay?
- **7944**: Item yooo don't know...everywhere, yes? Tumbling, tooopling, rooolling on the flooor, here and there, yes? Yooo happy to find them, yes?
- **7945**: Chochoroon thank yooo for clink clink.
- **7946**: Hmm hmm hmmm... This seems tooo be...
- **7947**: Oooh! It's $1! Yooo can have it now.

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

### Event 206

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 52 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    43 00 43 01 20 01 42  03 01 10 00 80 1E F0 FF   C.C. .B........
0010: FF 7F 6F 70 1D 01 80 5B  02 80 F8 FF FF 7F F8 FF  ..op...[........
0020: FF 7F 70 61 73 30 53 F8  FF FF 7F F8 FF FF 7F 70  ..pas0S........p
0030: 61 73 30 21 00                                    as0!.           
```

#### Opcodes

```
  0: 0x0001 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x0003 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0008 [0x03] Work_Zone[1] = 1*
  5: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0012 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0013 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=7662*)
    → "Nice adventooorer save Chochoroon, yes? Chochoroon very happy. Chochoroon give yooo present."
  9: 0x0017 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=842*
 10: 0x0026 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 11: 0x0033 [0x21] END_EVENT
 12: 0x0034 [0x00] END_REQSTACK()
```

### Event 260

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0035    |
| Data Size    | 100 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1E F0 FF  FF 7F 6F 70 5B 02 80 F8       .....op[...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 03 80 23 24  .......tlk0...#$
0050: 04 80 05 80 05 80 25 02  00 10 05 80 00 6A 00 1D  ......%......j..
0060: 06 80 23 1D 07 80 23 01  88 00 02 00 10 00 80 00  ..#...#.........
0070: 79 00 1D 08 80 23 01 88  00 02 00 10 09 80 00 88  y....#..........
0080: 00 1D 0A 80 23 01 88 00  5B 02 80 F8 FF FF 7F F8  ....#...[.......
0090: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x0035 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=842*
  4: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7939*)
    → "Chochoroon is appraiser, no? Yooo give Chochoroon item for appraisal, no? Chochoroon appraise for just $0 clink clink!"
  5: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004F [0x24] CREATE_DIALOG(message_id=7940*, default_option=0*, option_flags=0*)
    → "Appraise? [Appraise, yes?/Appraise, no!/Appraise...what?]"
  7: 0x0056 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0057 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006A
  9: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7941*)
    → "Appraise, okay? Chochoroon tell yooo mysterious item name for $0 gil, okay?"
 10: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=7942*)
    → "Chochoroon put item with your treasooor, okay? So leave rooom, okay? And make sure can have more than one of item, yes?"
 12: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0067 [0x01] GOTO 0x0088
 14: 0x006A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0079
 15: 0x0072 [0x1D] PRINT_EVENT_MESSAGE(message_id=7943*)
    → "Appraise, no? Bye bye, okay?"
 16: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0076 [0x01] GOTO 0x0088
 18: 0x0079 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0088
 19: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=7944*)
    → "Item yooo don't know...everywhere, yes? Tumbling, tooopling, rooolling on the flooor, here and there, yes? Yooo happy to find them, yes?"
 20: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0085 [0x01] GOTO 0x0088

SUBROUTINE_0088:
 22: 0x0088 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=842*
 23: 0x0097 [0x21] END_EVENT
 24: 0x0098 [0x00] END_REQSTACK()
```

### Event 261

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 52 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             42 1E F0 FF FF 7F 6F           B.....o
00A0: 70 5B 02 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  p[..........tlk0
00B0: 1D 0B 80 23 1D 0C 80 23  1D 0D 80 23 5B 02 80 F8  ...#...#...#[...
00C0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0099 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x009A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x009F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00A0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00A1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=842*
  5: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7945*)
    → "Chochoroon thank yooo for clink clink."
  6: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00B4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7946*)
    → "Hmm hmm hmmm... This seems tooo be..."
  8: 0x00B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00B8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7947*)
    → "Oooh! It's $1! Yooo can have it now."
 10: 0x00BB [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00BC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=842*
 12: 0x00CB [0x21] END_EVENT
 13: 0x00CC [0x00] END_REQSTACK()
```
