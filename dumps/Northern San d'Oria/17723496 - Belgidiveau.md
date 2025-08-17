# 17723496 - Belgidiveau

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 348 bytes                     |
| Total Events     | 6                             |
| References Count | 16                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [585](#event-585)     | 0x0001       |     43 |             13 |
| [57](#event-57)       | 0x002C       |    119 |             27 |
| [55](#event-55)       | 0x00A3       |     28 |              8 |
| [56](#event-56)       | 0x00BF       |     45 |              9 |
| [898](#event-898)     | 0x00EC       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2D0B      |       11531 |
|       2 | 0x001E      |          30 |
|       3 | 0x2D0C      |       11532 |
|       4 | 0x40000000  |  1073741824 |
|       5 | 0x2D0D      |       11533 |
|       6 | 0x2D0E      |       11534 |
|       7 | 0x2D0F      |       11535 |
|       8 | 0x2D10      |       11536 |
|       9 | 0x0001      |           1 |
|      10 | 0x0000      |           0 |
|      11 | 0x2D11      |       11537 |
|      12 | 0x2D12      |       11538 |
|      13 | 0x2D13      |       11539 |
|      14 | 0x2D14      |       11540 |
|      15 | 0x00C9      |         201 |

## String References

- **11531**: These sluice gates divide Northern San d'Oria into two parts: the Parade Grounds, and Laborman's Way.
- **11532**: Laborman's Way is much lower than the rest of the city. So to prevent flooding, we use these sluice gates to adjust the water for the entire district!
- **11533**: Wait, you're an adventurer, aren't you? I have a request, if you've the time...
- **11534**: Don't tell anyone, but someone sent me a letter saying they poisoned the water here! We're looking into the veracity of that claim now.
- **11535**: In the meantime, we must prepare a neutralizer to eliminate the poison. Might you be willing to obtain one?
- **11536**: Go fetch the neutralizer? [Let's do it./Not right now.]
- **11537**: That is good news, indeed! Now, all we need is someone versed in the ways of poison, but they're a hard lot to find...
- **11538**: Oh, we can't just let innocent people die from poisoned water now, can we?
- **11539**: It's no easy task, finding a neutralizer, is it? Few are skilled in the arts of poison, though that's a good thing, I suppose.
- **11540**: You've got the neutralizer! But, the thing is...it turns out it was all just a hoax. But we'll reward you anyway.

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

### Event 585

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1C 02 80 1D 03  ...tlk0...#.....
0020: 80 23 5E 69 64 6C 30 1C  02 80 21 00              .#^idl0...!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=11531*)
    → "These sluice gates divide Northern San d'Oria into two parts: the Parade Grounds, and Laborman's Way."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1C] WAIT(30* ticks)
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=11532*)
    → "Laborman's Way is much lower than the rest of the city. So to prevent flooding, we use these sluice gates to adjust the water for the entire district!"
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0027 [0x1C] WAIT(30* ticks)
 11: 0x002A [0x21] END_EVENT
 12: 0x002B [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002C    |
| Data Size    | 119 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      03 01 10 04              ....
0030: 80 1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8  ......opf.......
0040: FF FF 7F 74 6C 6B 30 1D  05 80 23 1D 06 80 23 1D  ...tlk0...#...#.
0050: 07 80 23 5E 69 64 6C 30  24 08 80 09 80 0A 80 25  ..#^idl0$......%
0060: 02 00 10 0A 80 00 83 00  03 01 10 0A 80 66 00 80  .............f..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 0B 80 23  ........tlk0...#
0080: 01 A1 00 02 00 10 09 80  00 A1 00 66 00 80 F8 FF  ...........f....
0090: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 0C 80 23 01 A1  ......tlk0...#..
00A0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x002C [0x03] Work_Zone[1] = 1073741824*
  1: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=11533*)
    → "Wait, you're an adventurer, aren't you? I have a request, if you've the time..."
  6: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=11534*)
    → "Don't tell anyone, but someone sent me a letter saying they poisoned the water here! We're looking into the veracity of that claim now."
  8: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=11535*)
    → "In the meantime, we must prepare a neutralizer to eliminate the poison. Might you be willing to obtain one?"
 10: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0053 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 12: 0x0058 [0x24] CREATE_DIALOG(message_id=11536*, default_option=1*, option_flags=0*)
    → "Go fetch the neutralizer? [Let's do it./Not right now.]"
 13: 0x005F [0x25] WAIT_DIALOG_SELECT()
 14: 0x0060 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0083
 15: 0x0068 [0x03] Work_Zone[1] = 0*
 16: 0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 17: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=11537*)
    → "That is good news, indeed! Now, all we need is someone versed in the ways of poison, but they're a hard lot to find..."
 18: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0080 [0x01] GOTO 0x00A1
 20: 0x0083 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A1
 21: 0x008B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 22: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=11538*)
    → "Oh, we can't just let innocent people die from poisoned water now, can we?"
 23: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x009E [0x01] GOTO 0x00A1

SUBROUTINE_00A1:
 25: 0x00A1 [0x21] END_EVENT
 26: 0x00A2 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          1E F0 FF FF 7F  6F 70 66 00 80 F8 FF FF     .....opf.....
00B0: 7F F8 FF FF 7F 74 6C 6B  30 1D 0D 80 23 21 00     .....tlk0...#!. 
```

#### Opcodes

```
  0: 0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00AA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=11539*)
    → "It's no easy task, finding a neutralizer, is it? Few are skilled in the arts of poison, though that's a good thing, I suppose."
  5: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00BD [0x21] END_EVENT
  7: 0x00BE [0x00] END_REQSTACK()
```

### Event 56

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               1E                 .
00C0: F0 FF FF 7F 6F 70 66 00  80 F8 FF FF 7F F8 FF FF  ....opf.........
00D0: 7F 74 6C 6B 30 1D 0E 80  23 45 0F 80 F0 FF FF 7F  .tlk0...#E......
00E0: F0 FF FF 7F 71 73 74 63  0A 80 21 00              ....qstc..!.    
```

#### Opcodes

```
  0: 0x00BF [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00D5 [0x1D] PRINT_EVENT_MESSAGE(message_id=11540*)
    → "You've got the neutralizer! But, the thing is...it turns out it was all just a hoax. But we'll reward you anyway."
  5: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00D9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  7: 0x00EA [0x21] END_EVENT
  8: 0x00EB [0x00] END_REQSTACK()
```

### Event 898

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EC  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      92 01 F8 FF              ....
00F0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00EC [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00F2 [0x00] END_REQSTACK()
```
