# 17723551 - Maloquedil

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 380 bytes                     |
| Total Events     | 6                             |
| References Count | 20                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |     11 |              3 |
| [21](#event-21)       | 0x000B       |     37 |             11 |
| [24](#event-24)       | 0x0030       |    108 |             31 |
| [22](#event-22)       | 0x009C       |     13 |              7 |
| [23](#event-23)       | 0x00A9       |     33 |             10 |
| [807](#event-807)     | 0x00CA       |     56 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x03FA      |        1018 |
|       1 | 0x0002      |           2 |
|       2 | 0x0014      |          20 |
|       3 | 0x2F48      |       12104 |
|       4 | 0x2F49      |       12105 |
|       5 | 0x0000      |           0 |
|       6 | 0x2F4A      |       12106 |
|       7 | 0x2F4C      |       12108 |
|       8 | 0x0001      |           1 |
|       9 | 0x2F4D      |       12109 |
|      10 | 0x2F4E      |       12110 |
|      11 | 0x2F4B      |       12107 |
|      12 | 0x2F4F      |       12111 |
|      13 | 0x2F50      |       12112 |
|      14 | 0x00C9      |         201 |
|      15 | 0x37EF      |       14319 |
|      16 | 0x001E      |          30 |
|      17 | 0x37F5      |       14325 |
|      18 | 0x37F6      |       14326 |
|      19 | 0x37F7      |       14327 |

## String References

- **12104**: There's a guard in the dungeon of Chateau d'Oraguille. Have you heard what they say of him?
- **12105**: They say he's a vampire! He dwells there perhaps to hide from the light. And there's plenty of adventurers to suck fresh blood from!
- **12106**: I have been eating $0 just to be safe. You don't think you could bring me $1, could you? I'll pay!
- **12107**: I still seek $1 $0 ! I cannot seem to get enough!
- **12108**: Accept his request? [Sure./No, thanks.]
- **12109**: What a relief! Eh? My breath a little strong for you? Well, I'll take halitosis over blood-sucking vampires any day!
- **12110**: Pity. I'll just hope to catch you later when you're not so "busy."
- **12111**: Those Orcish cursemakers in Davoi carry $0 sometimes. They use it as an ingredient for their spells, I hear.
- **12112**: Ah! I can't thank you enough. Here, take this... What, my breath? It's not that bad, is it?
- **14319**: <Player>'s badge flashes brightly.
- **14325**: Have you heard much about the company distributing those badges?
- **14326**: Their headquarters are in a Near Eastern town called "Al Zahbi." Rumor has it that the company president is something of a miser.
- **14327**: What could they possibly want with San d'Oria? You may want to think twice before clipping on one of those things.

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 02 10 00 80 03 03 10  01 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0000 [0x03] Work_Zone[2] = 1018*
  1: 0x0005 [0x03] Work_Zone[3] = 2*
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 37 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1E F0 FF FF 7F             .....
0010: 6F 70 66 02 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  opf..........tlk
0020: 30 1D 03 80 23 1D 04 80  23 5E 69 64 6C 30 21 00  0...#...#^idl0!.
```

#### Opcodes

```
  0: 0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0012 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=12104*)
    → "There's a guard in the dungeon of Chateau d'Oraguille. Have you heard what they say of him?"
  5: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=12105*)
    → "They say he's a vampire! He dwells there perhaps to hide from the light. And there's plenty of adventurers to suck fresh blood from!"
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0030    |
| Data Size    | 108 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 03 00 00 09 10 06 01 10  1E F0 FF FF 7F 6F 70 66  .............opf
0040: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 02 00  ..........tlk0..
0050: 00 05 80 00 96 00 1D 03  80 23 1D 04 80 23 1D 06  .........#...#..
0060: 80 23 5E 69 64 6C 30 24  07 80 08 80 05 80 25 02  .#^idl0$......%.
0070: 00 10 05 80 00 84 00 42  1D 09 80 23 03 01 10 08  .......B...#....
0080: 80 01 93 00 02 00 10 08  80 00 93 00 1D 0A 80 23  ...............#
0090: 01 93 00 01 9A 00 1D 0B  80 23 21 00              .........#!.    
```

#### Opcodes

```
  0: 0x0030 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[9]
  1: 0x0035 [0x06] Work_Zone[1] = 0
  2: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x003F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  6: 0x004E [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0096
  7: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=12104*)
    → "There's a guard in the dungeon of Chateau d'Oraguille. Have you heard what they say of him?"
  8: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=12105*)
    → "They say he's a vampire! He dwells there perhaps to hide from the light. And there's plenty of adventurers to suck fresh blood from!"
 10: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=12106*)
    → "I have been eating $0 just to be safe. You don't think you could bring me $1, could you? I'll pay!"
 12: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0062 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 14: 0x0067 [0x24] CREATE_DIALOG(message_id=12108*, default_option=1*, option_flags=0*)
    → "Accept his request? [Sure./No, thanks.]"
 15: 0x006E [0x25] WAIT_DIALOG_SELECT()
 16: 0x006F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0084
 17: 0x0077 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 18: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=12109*)
    → "What a relief! Eh? My breath a little strong for you? Well, I'll take halitosis over blood-sucking vampires any day!"
 19: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x007C [0x03] Work_Zone[1] = 1*
 21: 0x0081 [0x01] GOTO 0x0093
 22: 0x0084 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0093
 23: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=12110*)
    → "Pity. I'll just hope to catch you later when you're not so "busy.""
 24: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0090 [0x01] GOTO 0x0093

SUBROUTINE_0093:
 26: 0x0093 [0x01] GOTO 0x009A
 27: 0x0096 [0x1D] PRINT_EVENT_MESSAGE(message_id=12107*)
    → "I still seek $1 $0 ! I cannot seem to get enough!"
 28: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_009A:
 29: 0x009A [0x21] END_EVENT
 30: 0x009B [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      1E F0 FF FF              ....
00A0: 7F 6F 70 1D 0C 80 23 21  00                       .op...#!.       
```

#### Opcodes

```
  0: 0x009C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=12111*)
    → "Those Orcish cursemakers in Davoi carry $0 sometimes. They use it as an ingredient for their spells, I hear."
  4: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00A7 [0x21] END_EVENT
  6: 0x00A8 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 33 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             20 01 42 1E F0 FF FF            .B....
00B0: 7F 6F 70 1D 0D 80 23 45  0E 80 F0 FF FF 7F F0 FF  .op...#E........
00C0: FF 7F 71 73 74 63 05 80  21 00                    ..qstc..!.      
```

#### Opcodes

```
  0: 0x00A9 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00AB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00AC [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x00B3 [0x1D] PRINT_EVENT_MESSAGE(message_id=12112*)
    → "Ah! I can't thank you enough. Here, take this... What, my breath? It's not that bad, is it?"
  6: 0x00B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x00C8 [0x21] END_EVENT
  9: 0x00C9 [0x00] END_REQSTACK()
```

### Event 807

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 56 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                42 48 0F 80 1E F0            BH....
00D0: FF FF 7F 1C 10 80 1D 11  80 23 66 02 80 F8 FF FF  .........#f.....
00E0: 7F F8 FF FF 7F 74 6C 6B  30 1D 12 80 23 1D 13 80  .....tlk0...#...
00F0: 23 66 02 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  #f..........tlk1
0100: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00CA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00CB [0x48] [System] [14319*]:
    → "<Player>'s badge flashes brightly."
  2: 0x00CE [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00D3 [0x1C] WAIT(30* ticks)
  4: 0x00D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=14325*)
    → "Have you heard much about the company distributing those badges?"
  5: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00DA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  7: 0x00E9 [0x1D] PRINT_EVENT_MESSAGE(message_id=14326*)
    → "Their headquarters are in a Near Eastern town called "Al Zahbi." Rumor has it that the company president is something of a miser."
  8: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00ED [0x1D] PRINT_EVENT_MESSAGE(message_id=14327*)
    → "What could they possibly want with San d'Oria? You may want to think twice before clipping on one of those things."
 10: 0x00F0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00F1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 12: 0x0100 [0x21] END_EVENT
 13: 0x0101 [0x00] END_REQSTACK()
```
