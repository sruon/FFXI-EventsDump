# 17764498 - Etsa Rhuyuli

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 356 bytes                |
| Total Events     | 11                       |
| References Count | 10                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [65535.5](#event-655355) | 0x0045       |     29 |              3 |
| [65535.6](#event-655356) | 0x0062       |     16 |              2 |
| [65535.7](#event-655357) | 0x0072       |     14 |              2 |
| [65535.8](#event-655358) | 0x0080       |      9 |              3 |
| [422](#event-422)        | 0x0089       |     57 |             17 |
| [734](#event-734)        | 0x00C2       |     61 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x0051      |          81 |
|       3 | 0x2149      |        8521 |
|       4 | 0x214A      |        8522 |
|       5 | 0x214B      |        8523 |
|       6 | 0x28AF      |       10415 |
|       7 | 0x28B8      |       10424 |
|       8 | 0x28B9      |       10425 |
|       9 | 0x28BA      |       10426 |

## String References

- **8521**: The firrrst rrrule of the Starrr Onion Brrrigade...!
- **8522**: Show kindness to any stupid-looking adventurrrerrrs you meet!
- **8523**: It's firrrst come, firrrst serrrved when it comes to the items put on auction. You'rrre competing in bidding against people frrrom all overrr the worrrld, so don't hesitate if you'rrre not surrre. Just do it!
- **10415**: <Player>'s badge flashes brightly.
- **10424**: One rrrule of the Starrr Onion Brrrigade...!
- **10425**: Tell a special secrrret to any adventurer you meet wearrring a special badge!
- **10426**: The rrrumored "Salaheem's Sentinels" is located in the town of "Al Zahbi"!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  02 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 68 61 69 30 00                              ..hai0.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hai0" with entities [EventEntity, EventEntity], work=81*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 68 61 69 30 00                                    hai0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hai0" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 02 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 68 61 69 30 53 F8 FF FF  7F F8 FF FF 7F 68 61 69  hai0S........hai
0060: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hai0" with entities [EventEntity, EventEntity], work=81*
  1: 0x0054 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hai0" with entities [EventEntity, EventEntity]
  2: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       5B 02 80 F8 FF FF  7F F8 FF FF 7F 62 69 6B    [..........bik
0070: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0062 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=81*
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       53 F8 FF FF 7F F8  FF FF 7F 62 69 6B 30 00    S........bik0.
```

#### Opcodes

```
  0: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 5E 69 64 6C 30 1C 01 80  00                       ^idl0....       
```

#### Opcodes

```
  0: 0x0080 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0085 [0x1C] WAIT(30* ticks)
  2: 0x0088 [0x00] END_REQSTACK()
```

### Event 422

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 57 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             86 00 F8 FF FF 7F 1E           .......
0090: F0 FF FF 7F 6F 70 29 08  92 10 0F 01 03 1D 03 80  ....op).........
00A0: 23 29 08 92 10 0F 01 03  1D 04 80 23 29 08 92 10  #).........#)...
00B0: 0F 01 01 1D 05 80 23 29  08 92 10 0F 01 02 20 00  ......#)...... .
00C0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0089 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x008F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0095 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0096 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x03)
  5: 0x009D [0x1D] PRINT_EVENT_MESSAGE(message_id=8521*)
    → "The firrrst rrrule of the Starrr Onion Brrrigade...!"
  6: 0x00A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00A1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x03)
  8: 0x00A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=8522*)
    → "Show kindness to any stupid-looking adventurrrerrrs you meet!"
  9: 0x00AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00AC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x01)
 11: 0x00B3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8523*)
    → "It's firrrst come, firrrst serrrved when it comes to the items put on auction. You'rrre competing in bidding against people frrrom all overrr the worrrld, so don't hesitate if you'rrre not surrre. Just do it!"
 12: 0x00B6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00B7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x02)
 14: 0x00BE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x00C0 [0x21] END_EVENT
 16: 0x00C1 [0x00] END_REQSTACK()
```

### Event 734

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C2   |
| Data Size    | 61 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       42 48 06 80 86 00  F8 FF FF 7F 1E F0 FF FF    BH............
00D0: 7F 6F 70 29 08 92 10 0F  01 03 1D 07 80 23 29 08  .op).........#).
00E0: 92 10 0F 01 03 1D 08 80  23 29 08 92 10 0F 01 01  ........#)......
00F0: 1D 09 80 23 29 08 92 10  0F 01 02 20 00 21 00     ...#)...... .!. 
```

#### Opcodes

```
  0: 0x00C2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00C3 [0x48] [System] [10415*]:
    → "<Player>'s badge flashes brightly."
  2: 0x00C6 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  3: 0x00CC [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00D1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00D2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x00D3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x03)
  7: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=10424*)
    → "One rrrule of the Starrr Onion Brrrigade...!"
  8: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00DE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x03)
 10: 0x00E5 [0x1D] PRINT_EVENT_MESSAGE(message_id=10425*)
    → "Tell a special secrrret to any adventurer you meet wearrring a special badge!"
 11: 0x00E8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00E9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x01)
 13: 0x00F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10426*)
    → "The rrrumored "Salaheem's Sentinels" is located in the town of "Al Zahbi"!"
 14: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00F4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Etsa Rhuyuli (ID: 17764498/0x010F1092), tag_num=0x02)
 16: 0x00FB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x00FD [0x21] END_EVENT
 18: 0x00FE [0x00] END_REQSTACK()
```
