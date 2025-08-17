# 17760393 - Three of Clubs

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 104 bytes               |
| Total Events     | 5                       |
| References Count | 5                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      9 |              3 |
| [222](#event-222)        | 0x000B       |     19 |             10 |
| [625](#event-625)        | 0x001E       |     18 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0E38      |        3640 |
|       2 | 0x0E39      |        3641 |
|       3 | 0x3321      |       13089 |
|       4 | 0x332D      |       13101 |

## String References

- **3640**: WhAT$26tO$26Do$26IN$26sIt-U-A-tIOns$26lIkE$26tHIs!?
- **3641**: AA\`h! THrEE$26IS$26lOsInG$26cOn-Fi-DeNcE$26AS$26A$26gUaRd!
- **13089**: <Player>'s badge flashes brightly.
- **13101**: WhAT$26tO$26Do$26IN$26sIt-U-A-tIOns$26lIkE$26tHIs!? THaT$26iS$26nOT$26A$26FoOd!

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       5E 69 64 6C 30 1C  00 80 00                   ^idl0....     
```

#### Opcodes

```
  0: 0x0002 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0007 [0x1C] WAIT(30* ticks)
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 222

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1E F0 FF FF 7F             .....
0010: 6F 70 1D 01 80 23 1D 02  80 23 20 00 21 00        op...#...# .!.  
```

#### Opcodes

```
  0: 0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=3640*)
    → "WhAT$26tO$26Do$26IN$26sIt-U-A-tIOns$26lIkE$26tHIs!?"
  4: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=3641*)
    → "AA`h! THrEE$26IS$26lOsInG$26cOn-Fi-DeNcE$26AS$26A$26gUaRd!"
  6: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x001C [0x21] END_EVENT
  9: 0x001D [0x00] END_REQSTACK()
```

### Event 625

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            42 48                BH
0020: 03 80 1E F0 FF FF 7F 1C  00 80 1D 04 80 23 21 00  .............#!.
```

#### Opcodes

```
  0: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001F [0x48] [System] [13089*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0027 [0x1C] WAIT(30* ticks)
  4: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=13101*)
    → "WhAT$26tO$26Do$26IN$26sIt-U-A-tIOns$26lIkE$26tHIs!? THaT$26iS$26nOT$26A$26FoOd!"
  5: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002E [0x21] END_EVENT
  7: 0x002F [0x00] END_REQSTACK()
```
