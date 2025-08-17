# 17727553 - Bricorsant

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 188 bytes                 |
| Total Events     | 3                         |
| References Count | 11                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4](#event-4)         | 0x0001       |      1 |              1 |
| [570](#event-570)     | 0x0002       |    113 |             29 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1F1F      |        7967 |
|       2 | 0x1F20      |        7968 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFFFFFB  |  4294967291 |
|       5 | 0x0002      |           2 |
|       6 | 0x1F21      |        7969 |
|       7 | 0x001E      |          30 |
|       8 | 0x1F22      |        7970 |
|       9 | 0x0001      |           1 |
|      10 | 0x1F23      |        7971 |

## String References

- **7967**: Know your way around Port San d'Oria? Perhaps my map may be of service.
- **7968**: Look at the map? [Yes./No.]
- **7969**: Lufet Lake occupies half of Port San d'Oria. The travel agency and a pub lie at the north end of the wharf, and the auction house and cargo rooms at the south.
- **7970**: Head southeast for the Magicmart and residential area, or southwest for Laborman's Way in Northern San d'Oria.
- **7971**: As you wish.

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

### Event 4

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

### Event 570

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 113 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 5E 69 64 6C  ....tlk0...#^idl
0020: 30 24 02 80 03 80 03 80  25 02 00 10 03 80 00 4B  0$......%......K
0030: 00 8D 04 80 05 80 1D 06  80 23 1C 07 80 1D 08 80  .........#......
0040: 23 1C 07 80 8A 1C 07 80  01 71 00 02 00 10 09 80  #........q......
0050: 00 71 00 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .q.f..........tl
0060: 6B 30 1D 0A 80 23 5E 69  64 6C 30 1C 07 80 01 71  k0...#^idl0....q
0070: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "Know your way around Port San d'Oria? Perhaps my map may be of service."
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0021 [0x24] CREATE_DIALOG(message_id=7968*, default_option=0*, option_flags=0*)
    → "Look at the map? [Yes./No.]"
  8: 0x0028 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004B
 10: 0x0031 [0x8D] OPEN_MAP_WITH_PROPERTIES(map_id=4294967291*, properties=2*)
 11: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=7969*)
    → "Lufet Lake occupies half of Port San d'Oria. The travel agency and a pub lie at the north end of the wharf, and the auction house and cargo rooms at the south."
 12: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x003A [0x1C] WAIT(30* ticks)
 14: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "Head southeast for the Magicmart and residential area, or southwest for Laborman's Way in Northern San d'Oria."
 15: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0041 [0x1C] WAIT(30* ticks)
 17: 0x0044 [0x8A] CLOSE_MAP()
 18: 0x0045 [0x1C] WAIT(30* ticks)
 19: 0x0048 [0x01] GOTO 0x0071
 20: 0x004B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0071
 21: 0x0053 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 22: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "As you wish."
 23: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0066 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 25: 0x006B [0x1C] WAIT(30* ticks)
 26: 0x006E [0x01] GOTO 0x0071

SUBROUTINE_0071:
 27: 0x0071 [0x21] END_EVENT
 28: 0x0072 [0x00] END_REQSTACK()
```
