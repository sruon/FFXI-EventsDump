# 17834315 - Stout Weir

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 144 bytes                |
| Total Events     | 3                        |
| References Count | 5                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [373](#event-373)     | 0x0001       |     43 |              9 |
| [371](#event-371)     | 0x002C       |     52 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x2207      |        8711 |
|       2 | 0x2204      |        8708 |
|       3 | 0x2205      |        8709 |
|       4 | 0x2206      |        8710 |

## String References

- **8708**: So I was just here, mindin' my own business, see? Then all of a sudden, a huge flash of light, and boom! I darn near soiled m'self!
- **8709**: Th' area's gone a bit foul, and I'm 'fraid it'll take a while 'fore things're back to normal.
- **8710**: But boy, take a gander at this! It's part of a wooden fuse, wouldn't ya say? How crazy would ya hafta be to try to blow up the waterways!?
- **8711**: The waterways're vital to all who live in Adoulin, so don't be thinkin' 'bout causin' no trouble!

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

### Event 373

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 66 00 80 F8 FF  ...tlk0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8711*)
    → "The waterways're vital to all who live in Adoulin, so don't be thinkin' 'bout causin' no trouble!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=60*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 371

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 52 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      42 1E F0 FF              B...
0030: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0040: 6C 6B 30 1D 02 80 23 1D  03 80 23 1D 04 80 23 66  lk0...#...#...#f
0050: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x002C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  5: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=8708*)
    → "So I was just here, mindin' my own business, see? Then all of a sudden, a huge flash of light, and boom! I darn near soiled m'self!"
  6: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8709*)
    → "Th' area's gone a bit foul, and I'm 'fraid it'll take a while 'fore things're back to normal."
  8: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8710*)
    → "But boy, take a gander at this! It's part of a wooden fuse, wouldn't ya say? How crazy would ya hafta be to try to blow up the waterways!?"
 10: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x004F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=60*
 12: 0x005E [0x21] END_EVENT
 13: 0x005F [0x00] END_REQSTACK()
```
