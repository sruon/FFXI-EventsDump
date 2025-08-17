# 17793048 - Gabwaleid

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 232 bytes         |
| Total Events     | 3                 |
| References Count | 14                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [600](#event-600)     | 0x0001       |     28 |              8 |
| [601](#event-601)     | 0x001D       |    119 |             31 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x005A      |          90 |
|       1 | 0x1B41      |        6977 |
|       2 | 0x0005      |           5 |
|       3 | 0x0000      |           0 |
|       4 | 0x1B42      |        6978 |
|       5 | 0x0001      |           1 |
|       6 | 0x1B43      |        6979 |
|       7 | 0x0002      |           2 |
|       8 | 0x1B44      |        6980 |
|       9 | 0x0003      |           3 |
|      10 | 0x1B45      |        6981 |
|      11 | 0x0004      |           4 |
|      12 | 0x1B46      |        6982 |
|      13 | 0x1B47      |        6983 |

## String References

- **6977**: What can I do for you? I'm Gabwaleid. Someday I want to be a real fisherman like Zaldon.
- **6978**: You have to pick the right bait depending on what fish you want to catch. Otherwise it's all a waste!
- **6979**: You have to be aware of the time of day and the weather, too. Try to fish at the best time and under the best weather.
- **6980**: You'll catch different fish depending on where you are. Of course, there's a big difference between fishing from the river and from the sea.
- **6981**: Oh, and one more thing... It hardly ever happens, but once in a while something...unexpected may bite. Be careful!
- **6982**: There's nothing better than fishing from the ship. There are so many unique things to catch. The time just flies!
- **6983**: There's nothing wrong with bait, but I go for lures, myself. You can keep using them till your line breaks or your pole snaps. Of course, they cost more.

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

### Event 600

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 21 00           ...tlk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=90*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=6977*)
    → "What can I do for you? I'm Gabwaleid. Someday I want to be a real fisherman like Zaldon."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()
```

### Event 601

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x001D    |
| Data Size    | 119 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         1E F0 FF               ...
0020: FF 7F 13 00 00 02 80 6F  70 5B 00 80 F8 FF FF 7F  .......op[......
0030: F8 FF FF 7F 74 6C 6B 30  02 00 00 03 80 80 47 00  ....tlk0......G.
0040: 1D 04 80 23 01 92 00 02  00 00 05 80 80 56 00 1D  ...#.........V..
0050: 06 80 23 01 92 00 02 00  00 07 80 80 65 00 1D 08  ..#.........e...
0060: 80 23 01 92 00 02 00 00  09 80 80 74 00 1D 0A 80  .#.........t....
0070: 23 01 92 00 02 00 00 0B  80 80 83 00 1D 0C 80 23  #..............#
0080: 01 92 00 02 00 00 02 80  80 92 00 1D 0D 80 23 01  ..............#.
0090: 92 00 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x001D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0022 [0x13] ExtData[1]->WorkLocal[0] = rand() % 5*
  2: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0028 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0029 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=90*
  5: 0x0038 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0047
  6: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=6978*)
    → "You have to pick the right bait depending on what fish you want to catch. Otherwise it's all a waste!"
  7: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0044 [0x01] GOTO 0x0092
  9: 0x0047 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0056
 10: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=6979*)
    → "You have to be aware of the time of day and the weather, too. Try to fish at the best time and under the best weather."
 11: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0053 [0x01] GOTO 0x0092
 13: 0x0056 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0065
 14: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=6980*)
    → "You'll catch different fish depending on where you are. Of course, there's a big difference between fishing from the river and from the sea."
 15: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0062 [0x01] GOTO 0x0092
 17: 0x0065 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0074
 18: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=6981*)
    → "Oh, and one more thing... It hardly ever happens, but once in a while something...unexpected may bite. Be careful!"
 19: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0071 [0x01] GOTO 0x0092
 21: 0x0074 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x0083
 22: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=6982*)
    → "There's nothing better than fishing from the ship. There are so many unique things to catch. The time just flies!"
 23: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0080 [0x01] GOTO 0x0092
 25: 0x0083 [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x0092
 26: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=6983*)
    → "There's nothing wrong with bait, but I go for lures, myself. You can keep using them till your line breaks or your pole snaps. Of course, they cost more."
 27: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x008F [0x01] GOTO 0x0092

SUBROUTINE_0092:
 29: 0x0092 [0x21] END_EVENT
 30: 0x0093 [0x00] END_REQSTACK()
```
