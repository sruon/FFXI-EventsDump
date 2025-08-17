# 17748171 - Matrimonial Coffer

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 184 bytes            |
| Total Events     | 2                    |
| References Count | 8                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2000](#event-2000)   | 0x0001       |    127 |             32 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2A62      |       10850 |
|       1 | 0x2A63      |       10851 |
|       2 | 0x0000      |           0 |
|       3 | 0x2A65      |       10853 |
|       4 | 0x2A64      |       10852 |
|       5 | 0x0001      |           1 |
|       6 | 0x0064      |         100 |
|       7 | 0x2A66      |       10854 |

## String References

- **10850**: An assortment of wedding attire and wedding rings are available for purchase.
- **10851**: What will you buy? [[Wedding dress/Benedight] set: $1 gil./$2: $3 gil./Nothing.]
- **10852**: This set includes a benedight coat and a pair of benedight hose. Price: $1 gil.
- **10853**: This set includes a bridal corsage, a wedding dress, a pair of wedding hose, and a pair of wedding boots. Price: $1 gil.
- **10854**: Confirm purchase? (Current gil: $4) [Yes./Cancel.]

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

### Event 2000

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 127 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 48 00 80 23 24 01   J........H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 3F 00 03 01  .....%......?...
0020: 10 02 80 02 02 10 02 80  00 35 00 48 03 80 23 1A  .........5.H..#.
0030: 59 00 01 3C 00 48 04 80  23 1A 59 00 01 57 00 02  Y..<.H..#.Y..W..
0040: 00 10 05 80 00 52 00 03  01 10 05 80 1A 59 00 01  .....R.......Y..
0050: 57 00 03 01 10 06 80 21  00 24 07 80 05 80 02 80  W......!.$......
0060: 25 02 00 10 02 80 00 6F  00 0B 01 10 01 7F 00 02  %......o........
0070: 00 10 05 80 00 7F 00 03  01 10 06 80 01 7F 00 1B  ................
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x48] [System] [10850*]:
    → "An assortment of wedding attire and wedding rings are available for purchase."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=10851*, default_option=0*, option_flags=0*)
    → "What will you buy? [[Wedding dress/Benedight] set: $1 gil./$2: $3 gil./Nothing.]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003F
  6: 0x001E [0x03] Work_Zone[1] = 0*
  7: 0x0023 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0035
  8: 0x002B [0x48] [System] [10853*]:
    → "This set includes a bridal corsage, a wedding dress, a pair of wedding hose, and a pair of wedding boots. Price: $1 gil."
  9: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002F [0x1A] CALL_SUBROUTINE(address=0x0059)
 11: 0x0032 [0x01] GOTO 0x003C
 12: 0x0035 [0x48] [System] [10852*]:
    → "This set includes a benedight coat and a pair of benedight hose. Price: $1 gil."
 13: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0039 [0x1A] CALL_SUBROUTINE(address=0x0059)

SUBROUTINE_003C:
 15: 0x003C [0x01] GOTO 0x0057
 16: 0x003F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0052
 17: 0x0047 [0x03] Work_Zone[1] = 1*
 18: 0x004C [0x1A] CALL_SUBROUTINE(address=0x0059)
 19: 0x004F [0x01] GOTO 0x0057
 20: 0x0052 [0x03] Work_Zone[1] = 100*

SUBROUTINE_0057:
 21: 0x0057 [0x21] END_EVENT
 22: 0x0058 [0x00] END_REQSTACK()

SUBROUTINE_0059:
 23: 0x0059 [0x24] CREATE_DIALOG(message_id=10854*, default_option=1*, option_flags=0*)
    → "Confirm purchase? (Current gil: $4) [Yes./Cancel.]"
 24: 0x0060 [0x25] WAIT_DIALOG_SELECT()
 25: 0x0061 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006F
 26: 0x0069 [0x0B] Work_Zone[1]++
 27: 0x006C [0x01] GOTO 0x007F
 28: 0x006F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007F
 29: 0x0077 [0x03] Work_Zone[1] = 100*
 30: 0x007C [0x01] GOTO 0x007F

SUBROUTINE_007F:
 31: 0x007F [0x1B] RETURN
```
