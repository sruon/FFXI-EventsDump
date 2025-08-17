# 17756251 - Naih Arihmepp

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 184 bytes                |
| Total Events     | 6                        |
| References Count | 7                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [326](#event-326)        | 0x0021       |     39 |             13 |
| [500](#event-500)        | 0x0048       |     43 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F0A      |        7946 |
|       3 | 0x1F0B      |        7947 |
|       4 | 0x2588      |        9608 |
|       5 | 0x2594      |        9620 |
|       6 | 0x2595      |        9621 |

## String References

- **7946**: I'm sure you've seen the automaton guards positioned all around Windurrrst. You had better take carrre when dealing with those Cardians.
- **7947**: This is just between you and me, but those machines go crrrazy sometimes. I've even heard that there have been Tarutaru kidnapped by the malfunctioning Carrrdians!
- **9608**: <Player>'s badge flashes brightly.
- **9620**: You had better take carrre when dealing with the Cardians. This is just between you and me, but those machines go crrrazy sometimes.
- **9621**: I've heard that there are similar creations in the Near East. I wonder if they have the same prrroblems...

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 326

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 29 0B   ...........op).
0030: 5B F0 0E 01 01 1D 02 80  23 1D 03 80 23 29 0B 5B  [.......#...#).[
0040: F0 0E 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0021 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Naih Arihmepp (ID: 17756251/0x010EF05B), tag_num=0x01)
  5: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7946*)
    → "I'm sure you've seen the automaton guards positioned all around Windurrrst. You had better take carrre when dealing with those Cardians."
  6: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7947*)
    → "This is just between you and me, but those machines go crrrazy sometimes. I've even heard that there have been Tarutaru kidnapped by the malfunctioning Carrrdians!"
  8: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Naih Arihmepp (ID: 17756251/0x010EF05B), tag_num=0x02)
 10: 0x0044 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0046 [0x21] END_EVENT
 12: 0x0047 [0x00] END_REQSTACK()
```

### Event 500

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 43 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          42 48 04 80 86 00 F8 FF          BH......
0050: FF 7F 1E F0 FF FF 7F 6F  70 29 0B 5B F0 0E 01 01  .......op).[....
0060: 1D 05 80 23 1D 06 80 23  29 0B 5B F0 0E 01 02 20  ...#...#).[.... 
0070: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0048 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0049 [0x48] [System] [9608*]:
    → "<Player>'s badge flashes brightly."
  2: 0x004C [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  3: 0x0052 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0058 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0059 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Naih Arihmepp (ID: 17756251/0x010EF05B), tag_num=0x01)
  7: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=9620*)
    → "You had better take carrre when dealing with the Cardians. This is just between you and me, but those machines go crrrazy sometimes."
  8: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=9621*)
    → "I've heard that there are similar creations in the Near East. I wonder if they have the same prrroblems..."
 10: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0068 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Naih Arihmepp (ID: 17756251/0x010EF05B), tag_num=0x02)
 12: 0x006F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0071 [0x21] END_EVENT
 14: 0x0072 [0x00] END_REQSTACK()
```
